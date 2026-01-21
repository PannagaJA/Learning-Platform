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
def admin_dashboard(request):
    """
    Admin dashboard endpoint
    """
    if not request.user.is_admin:
        return Response({'error': 'Only admins can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    # Count various entities
    user_count = User.objects.count()
    dept_count = Department.objects.count()
    semester_count = Semester.objects.count()
    section_count = Section.objects.count()
    subject_count = Subject.objects.count()
    
    data = {
        'user_count': user_count,
        'department_count': dept_count,
        'semester_count': semester_count,
        'section_count': section_count,
        'subject_count': subject_count,
        'message': f'Welcome, {request.user.username}!'
    }
    
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_users(request):
    """
    Manage all users in the system
    """
    if not request.user.is_admin:
        return Response({'error': 'Only admins can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Admin can create users with specific roles
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_single_user(request, user_id):
    """
    Manage a specific user
    """
    if not request.user.is_admin:
        return Response({'error': 'Only admins can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_departments(request):
    """
    Manage departments
    """
    if not request.user.is_admin:
        return Response({'error': 'Only admins can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        depts = Department.objects.all()
        from users.serializers import DepartmentSerializer
        serializer = DepartmentSerializer(depts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        from users.serializers import DepartmentSerializer
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            dept = serializer.save()
            return Response(DepartmentSerializer(dept).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_single_department(request, dept_id):
    """
    Manage a specific department
    """
    if not request.user.is_admin:
        return Response({'error': 'Only admins can access this endpoint'}, 
                       status=status.HTTP_403_FORBIDDEN)
    
    try:
        dept = Department.objects.get(id=dept_id)
    except Department.DoesNotExist:
        return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        from users.serializers import DepartmentSerializer
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        from users.serializers import DepartmentSerializer
        serializer = DepartmentSerializer(dept, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        dept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)