from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Authentication URLs
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    # User management URLs
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]