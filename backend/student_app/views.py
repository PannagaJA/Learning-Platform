from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from users.models import Department, Semester, Section, Subject, Attendance, Notification
from users.serializers import UserSerializer

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_dashboard(request):
    """
    Student dashboard endpoint
    """
    if not request.user.is_student:
        return Response({'error': 'Only students can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    # Get student-specific data
    student_section = request.user.section
    student_subjects = Subject.objects.filter(semesters=student_section.semester) if student_section else []
    
    data = {
        'student_name': request.user.get_full_name(),
        'department': request.user.department.name if request.user.department else None,
        'semester': student_section.semester.name if student_section else None,
        'section': student_section.name if student_section else None,
        'enrolled_subjects': len(student_subjects),
        'message': f'Welcome, {request.user.username}!'
    }
    
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_attendance(request):
    """
    Get attendance records for the logged-in student
    """
    if not request.user.is_student:
        return Response({'error': 'Only students can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    subject_id = request.query_params.get('subject_id')
    
    attendances = Attendance.objects.filter(student=request.user)
    
    if subject_id:
        attendances = attendances.filter(subject_id=subject_id)
    
    # Calculate attendance percentage
    total_classes = attendances.count()
    present_classes = attendances.filter(is_present=True).count()
    attendance_percentage = (present_classes / total_classes * 100) if total_classes > 0 else 0
    
    attendance_data = []
    for attendance in attendances:
        attendance_data.append({
            'id': attendance.id,
            'subject': attendance.subject.name,
            'date': attendance.date,
            'is_present': attendance.is_present,
            'marked_by': attendance.marked_by.username
        })
    
    response_data = {
        'attendance_records': attendance_data,
        'total_classes': total_classes,
        'present_classes': present_classes,
        'absent_classes': total_classes - present_classes,
        'attendance_percentage': round(attendance_percentage, 2)
    }
    
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_subjects(request):
    """
    Get subjects enrolled by the student
    """
    if not request.user.is_student:
        return Response({'error': 'Only students can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    student_section = request.user.section
    if not student_section:
        return Response({'error': 'Student is not assigned to a section'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    subjects = Subject.objects.filter(semesters=student_section.semester)
    
    subject_data = []
    for subject in subjects:
        # Calculate attendance for each subject
        subject_attendance = Attendance.objects.filter(
            student=request.user,
            subject=subject
        )
        total_classes = subject_attendance.count()
        present_classes = subject_attendance.filter(is_present=True).count()
        attendance_percentage = (present_classes / total_classes * 100) if total_classes > 0 else 0
        
        subject_data.append({
            'id': subject.id,
            'name': subject.name,
            'code': subject.code,
            'faculty': subject.faculty.get_full_name() if subject.faculty else None,
            'total_classes': total_classes,
            'present_classes': present_classes,
            'attendance_percentage': round(attendance_percentage, 2)
        })
    
    return Response(subject_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_notifications(request):
    """
    Get notifications for the logged-in student
    """
    if not request.user.is_student:
        return Response({'error': 'Only students can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at')
    
    notification_data = []
    for notification in notifications:
        notification_data.append({
            'id': notification.id,
            'title': notification.title,
            'message': notification.message,
            'notification_type': notification.notification_type,
            'is_read': notification.is_read,
            'created_at': notification.created_at,
            'sender': notification.sender.get_full_name() if notification.sender else None
        })
    
    return Response(notification_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_notification_as_read(request, notification_id):
    """
    Mark a specific notification as read
    """
    if not request.user.is_student:
        return Response({'error': 'Only students can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    try:
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return Response({'message': 'Notification marked as read'})
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)