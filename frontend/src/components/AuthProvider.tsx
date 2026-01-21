import React, { useEffect } from 'react';
import { useAuthStore } from '../store/authStore';

interface AuthProviderProps {
  children: React.ReactNode;
}

const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const { getCurrentUser, isAuthenticated } = useAuthStore();

  useEffect(() => {
    // Attempt to get current user on app initialization
    const fetchUser = async () => {
      try {
        // Only try to get current user if we have a token stored
        const token = localStorage.getItem('access_token');
        if (token && !isAuthenticated) {
          await getCurrentUser();
        }
      } catch (error) {
        // Silently handle case where user is not authenticated
        console.log('No authenticated user or token expired');
      }
    };
    
    fetchUser();
  }, [getCurrentUser, isAuthenticated]);

  return <>{children}</>;
};

export default AuthProvider;