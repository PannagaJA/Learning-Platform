import React, { useState, useEffect } from 'react';
import { useAuthStore } from '../../store/authStore';
import { authService } from '../../services/authService';

const AdminDashboard: React.FC = () => {
  const { user } = useAuthStore();
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await authService.getCurrentUser();
        // For now, we'll just display user info until we have the full admin stats API
        setStats({
          totalUsers: 0,
          totalDepartments: 0,
          totalSemesters: 0,
          totalSections: 0,
          totalSubjects: 0,
          totalAttendanceRecords: 0
        });
        setLoading(false);
      } catch (err) {
        setError('Failed to load statistics');
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white p-6 rounded-lg shadow">
        <div className="text-red-500 text-center py-8">{error}</div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Admin Dashboard</h2>
        <p className="text-gray-600">Welcome back, {user?.username}!</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold text-gray-700">Total Users</h3>
          <p className="text-3xl font-bold text-blue-600 mt-2">{stats?.totalUsers || 0}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold text-gray-700">Departments</h3>
          <p className="text-3xl font-bold text-green-600 mt-2">{stats?.totalDepartments || 0}</p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold text-gray-700">Subjects</h3>
          <p className="text-3xl font-bold text-purple-600 mt-2">{stats?.totalSubjects || 0}</p>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-semibold text-gray-700 mb-4">Quick Actions</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <button className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded transition duration-200">
            Manage Users
          </button>
          <button className="bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded transition duration-200">
            Manage Departments
          </button>
          <button className="bg-yellow-500 hover:bg-yellow-600 text-white py-2 px-4 rounded transition duration-200">
            View Reports
          </button>
          <button className="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded transition duration-200">
            System Settings
          </button>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;