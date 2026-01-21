import { create } from 'zustand';
import { authService } from '../services/authService';
import React from 'react';

interface User {
  id: number;
  username: string;
  email: string;
  first_name?: string;
  last_name?: string;
  role: string;
  department?: string;
  is_active: boolean;
  date_joined: string;
  last_login?: string;
}

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
  
  // Authentication actions
  login: (username: string, password: string) => Promise<void>;
  register: (userData: {
    username: string;
    email: string;
    password: string;
    password_confirm: string;
    first_name?: string;
    last_name?: string;
    role: string;
    department?: number;
  }) => Promise<void>;
  logout: () => Promise<void>;
  getCurrentUser: () => Promise<void>;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: false,
  error: null,

  login: async (username: string, password: string) => {
    set({ isLoading: true, error: null });
    try {
      const data = await authService.login(username, password);
      set({ 
        user: data.user, 
        isAuthenticated: true, 
        isLoading: false 
      });
    } catch (error: any) {
      set({ 
        error: error.message || 'Login failed', 
        isLoading: false 
      });
      throw error;
    }
  },

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
    set({ isLoading: true, error: null });
    try {
      const data = await authService.register(userData);
      set({ 
        user: data.user, 
        isAuthenticated: true, 
        isLoading: false 
      });
    } catch (error: any) {
      set({ 
        error: error.message || 'Registration failed', 
        isLoading: false 
      });
      throw error;
    }
  },

  logout: async () => {
    set({ isLoading: true });
    try {
      await authService.logout();
      set({ 
        user: null, 
        isAuthenticated: false, 
        isLoading: false 
      });
    } catch (error: any) {
      set({ 
        error: error.message || 'Logout failed', 
        isLoading: false 
      });
    }
  },

  getCurrentUser: async () => {
    set({ isLoading: true });
    try {
      const user = await authService.getCurrentUser();
      set({ 
        user, 
        isAuthenticated: true, 
        isLoading: false 
      });
    } catch (error: any) {
      set({ 
        error: error.message || 'Failed to get user data', 
        isLoading: false,
        user: null,
        isAuthenticated: false
      });
    }
  },

  clearError: () => set({ error: null }),
}));
