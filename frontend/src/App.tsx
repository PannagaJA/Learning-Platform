import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/layout/Layout';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import ProtectedRoute from './components/layout/ProtectedRoute';
import AdminDashboard from './pages/admin/AdminDashboard';

const App: React.FC = () => {
  return (
      <Router>
        <Layout>
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route 
              path="/" 
              element={
                <ProtectedRoute allowedRoles={['admin', 'hod', 'faculty', 'student']}>
                  <Dashboard />
                </ProtectedRoute>
              } 
            />
            <Route 
              path="/dashboard" 
              element={
                <ProtectedRoute allowedRoles={['admin', 'hod', 'faculty', 'student']}>
                  <Dashboard />
                </ProtectedRoute>
              } 
            />
            <Route 
              path="/admin" 
              element={
                <ProtectedRoute allowedRoles={['admin']}>
                  <AdminDashboard />
                </ProtectedRoute>
              } 
            />
            {/* Add more routes as needed */}
          </Routes>
        </Layout>
      </Router>
  );
};

export default App;