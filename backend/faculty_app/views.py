from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from users.models import Department, Semester, Section, Subject, Attendance
from users.serializers import UserSerializer

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def faculty_dashboard(request):
    """
    Faculty dashboard endpoint
    """
    if not request.user.is_faculty:
        return Response({'error': 'Only faculty members can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    # Get faculty-specific data
    faculty_subjects = Subject.objects.filter(faculty=request.user)
    assigned_sections = Section.objects.filter(subjects__faculty=request.user).distinct()
    
    data = {
        'faculty_name': request.user.get_full_name(),
        'department': request.user.department.name if request.user.department else None,
        'subjects_taught': faculty_subjects.count(),
        'sections_assigned': assigned_sections.count(),
        'message': f'Welcome, {request.user.username}!'
    }
    
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_students(request):
    """
    Get students in sections assigned to this faculty
    """
    if not request.user.is_faculty:
        return Response({'error': 'Only faculty members can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    # Get sections assigned to this faculty through subjects
    sections = Section.objects.filter(subjects__faculty=request.user).distinct()
    students = User.objects.filter(section__in=sections, role='student')
    
    serializer = UserSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_attendance(request):
    """
    Mark attendance for students in a particular class
    """
    if not request.user.is_faculty:
        return Response({'error': 'Only faculty members can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    # Expected data: { 'date': 'YYYY-MM-DD', 'section_id': id, 'subject_id': id, 'present_student_ids': [1, 2, 3] }
    date = request.data.get('date')
    section_id = request.data.get('section_id')
    subject_id = request.data.get('subject_id')
    present_student_ids = request.data.get('present_student_ids', [])
    
    if not all([date, section_id, subject_id]):
        return Response({'error': 'Date, section_id, and subject_id are required'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    try:
        from datetime import datetime
        from django.utils.dateparse import parse_date
        
        attendance_date = parse_date(date)
        section = Section.objects.get(id=section_id)
        subject = Subject.objects.get(id=subject_id)
        
        # Verify that the faculty teaches this subject in this section
        if subject.faculty != request.user or subject not in section.subjects.all():
            return Response({'error': 'You are not authorized to mark attendance for this class'}, 
                           status=status.HTTP_403_FORBIDDEN)
        
        # Get all students in the section
        students = User.objects.filter(section=section, role='student')
        
        # Mark attendance for each student
        for student in students:
            is_present = student.id in present_student_ids
            attendance, created = Attendance.objects.get_or_create(
                student=student,
                subject=subject,
                date=attendance_date,
                defaults={'is_present': is_present, 'marked_by': request.user}
            )
            if not created:
                attendance.is_present = is_present
                attendance.marked_by = request.user
                attendance.save()
        
        return Response({'message': f'Attendance marked for {len(students)} students'})
    
    except Section.DoesNotExist:
        return Response({'error': 'Section not found'}, status=status.HTTP_404_NOT_FOUND)
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_attendance_records(request):
    """
    Get attendance records for faculty's subjects
    """
    if not request.user.is_faculty:
        return Response({'error': 'Only faculty members can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    subject_id = request.query_params.get('subject_id')
    section_id = request.query_params.get('section_id')
    date_from = request.query_params.get('date_from')
    date_to = request.query_params.get('date_to')
    
    attendances = Attendance.objects.filter(subject__faculty=request.user)
    
    if subject_id:
        attendances = attendances.filter(subject_id=subject_id)
    if section_id:
        attendances = attendances.filter(student__section_id=section_id)
    if date_from:
        from django.utils.dateparse import parse_date
        attendances = attendances.filter(date__gte=parse_date(date_from))
    if date_to:
        from django.utils.dateparse import parse_date
        attendances = attendances.filter(date__lte=parse_date(date_to))
    
    # This would typically return aggregated data
    attendance_data = []
    for attendance in attendances[:50]:  # Limit for performance
        attendance_data.append({
            'id': attendance.id,
            'student': attendance.student.username,
            'student_name': attendance.student.get_full_name(),
            'subject': attendance.subject.name,
            'date': attendance.date,
            'is_present': attendance.is_present,
            'marked_by': attendance.marked_by.username
        })
    
    return Response(attendance_data)