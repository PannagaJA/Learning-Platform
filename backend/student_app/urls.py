from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student-dashboard'),
    path('attendance/', views.my_attendance, name='my-attendance'),
    path('subjects/', views.my_subjects, name='my-subjects'),
    path('notifications/', views.my_notifications, name='my-notifications'),
    path('notifications/<int:notification_id>/read/', views.mark_notification_as_read, name='mark-notification-read'),
]