from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.faculty_dashboard, name='faculty-dashboard'),
    path('students/', views.my_students, name='my-students'),
    path('attendance/mark/', views.mark_attendance, name='mark-attendance'),
    path('attendance/', views.get_attendance_records, name='get-attendance-records'),
]