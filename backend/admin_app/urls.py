from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('users/', views.manage_users, name='manage-users'),
    path('users/<int:user_id>/', views.manage_single_user, name='manage-single-user'),
    path('departments/', views.manage_departments, name='manage-departments'),
    path('departments/<int:dept_id>/', views.manage_single_department, name='manage-single-department'),
]