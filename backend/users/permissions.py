from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Permission class to allow access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsHODUser(permissions.BasePermission):
    """
    Permission class to allow access only to HOD users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'hod'


class IsFacultyUser(permissions.BasePermission):
    """
    Permission class to allow access only to faculty users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'faculty'


class IsStudentUser(permissions.BasePermission):
    """
    Permission class to allow access only to student users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsSameDepartment(permissions.BasePermission):
    """
    Permission class to check if requesting user belongs to same department as the resource.
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'department'):
            return obj.department == request.user.department
        elif hasattr(request.user, 'department'):
            # For cases where we're checking against the user's own department
            return obj == request.user.department
        return False


class CanModifyUser(permissions.BasePermission):
    """
    Permission class to control which users can modify other user accounts based on role hierarchy.
    """
    def has_object_permission(self, request, view, obj):
        # Users can always modify their own profiles
        if obj.id == request.user.id:
            return True
        
        # Admins can modify any user
        if request.user.role == 'admin':
            return True
        
        # HODs can modify faculty and students in their department
        if request.user.role == 'hod':
            if obj.department == request.user.department:
                return obj.role in ['faculty', 'student']
        
        # Faculty can modify students in their assigned classes
        if request.user.role == 'faculty':
            # This would need to be expanded based on specific faculty-student relationships
            if obj.role == 'student':
                # Check if the student is in a class the faculty teaches
                # This would require additional checks based on the subject/section relationship
                return obj.department == request.user.department
        
        return False