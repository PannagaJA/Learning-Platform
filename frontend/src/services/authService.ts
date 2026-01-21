import axios, { AxiosRequestConfig, AxiosResponse, InternalAxiosRequestConfig } from 'axios';

const API_BASE_URL = (import.meta as any).env.VITE_API_URL || 'http://localhost:8000/api/v1';

// Create an axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
});

// Request interceptor to add token to headers
api.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error: any) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle token refresh
api.interceptors.response.use(
  (response: AxiosResponse) => response,
  async (error: any) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        const refreshToken = localStorage.getItem('refresh_token');
        if (refreshToken) {
          const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, {
            refresh: refreshToken,
          });
          
          const { access } = response.data;
          localStorage.setItem('access_token', access);
          
          originalRequest.headers.Authorization = `Bearer ${access}`;
          return api(originalRequest);
        }
      } catch (refreshError) {
        // If refresh fails, redirect to login
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login';
      }
    }

    return Promise.reject(error);
  }
);

// Authentication service functions
export const authService = {
  // Login function
  login: async (username: string, password: string) => {
    try {
      const response = await api.post('/auth/login/', {
        username,
        password,
      });
      
      // Store tokens
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
      
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Login failed');
    }
  },

  // Logout function
  logout: async () => {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      if (refreshToken) {
        await api.post('/auth/logout/', {
          refresh: refreshToken,
        });
      }
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      // Remove tokens regardless of logout API success
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    }
  },

  // Register function
  register: async (userData: {
    username: string;
    email: string;
    password: string;
    password_confirm: string;
    first_name?: string;
    last_name?: string;
    role: string;
    department?: number;
  }) => {
    try {
      const response = await api.post('/auth/register/', userData);
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Registration failed');
    }
  },

  // Get current user
  getCurrentUser: async () => {
    try {
      const response = await api.get('/profile/');
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Failed to get user data');
    }
  },

  // Refresh token
  refreshToken: async () => {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      if (!refreshToken) {
        throw new Error('No refresh token available');
      }

      const response = await api.post('/auth/token/refresh/', {
        refresh: refreshToken,
      });

      const { access } = response.data;
      localStorage.setItem('access_token', access);
      
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || 'Token refresh failed');
    }
  },
};

export default api;