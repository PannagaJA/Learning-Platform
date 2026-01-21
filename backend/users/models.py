from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Adds role, department, semester, and section fields.
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hod', 'Head of Department'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.ForeignKey('Semester', on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Department(models.Model):
    """
    Department model representing academic departments.
    """
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    hod = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        limit_choices_to={'role': 'hod'},
        related_name='department_hod'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Departments"
    
    def __str__(self):
        return self.name


class Semester(models.Model):
    """
    Semester model representing academic semesters.
    """
    number = models.IntegerField(choices=[(i, i) for i in range(1, 9)])  # 1-8 semesters
    academic_year = models.CharField(max_length=10)  # e.g., "2023-24"
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['number', 'academic_year', 'department']
        verbose_name_plural = "Semesters"
    
    def __str__(self):
        return f"Semester {self.number} - {self.academic_year} ({self.department.code})"


class Section(models.Model):
    """
    Section model representing class sections (A, B, C, etc.).
    """
    name = models.CharField(max_length=10)  # A, B, C, etc.
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculty_incharge = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        limit_choices_to={'role': 'faculty'},
        related_name='section_incharge'
    )
    student_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['name', 'semester']
        verbose_name_plural = "Sections"
    
    def __str__(self):
        return f"{self.name} - {self.semester}"


class Subject(models.Model):
    """
    Subject model representing academic subjects/courses.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty_assigned = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        limit_choices_to={'role': 'faculty'},
        related_name='assigned_subjects'
    )
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['code', 'semester', 'department']
        verbose_name_plural = "Subjects"
    
    def __str__(self):
        return f"{self.name} ({self.code})"


class Notification(models.Model):
    """
    Notification model for system notifications.
    """
    title = models.CharField(max_length=200)
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    
    RECIPIENT_ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hod', 'HOD'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
        ('all', 'All'),
    ]
    
    recipient_role = models.CharField(max_length=20, choices=RECIPIENT_ROLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Notifications"
        ordering = ['-sent_at']
    
    def __str__(self):
        return f"{self.title} - {self.recipient_role}"


class AuditLog(models.Model):
    """
    AuditLog model for tracking user actions.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)  # e.g., 'user', 'department', 'subject'
    resource_id = models.IntegerField()  # ID of the resource affected
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Audit Logs"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.action}"


class Attendance(models.Model):
    """
    Attendance model for tracking student attendance.
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    marked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='attendance_marked', default=None)
    marked_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['student', 'subject', 'date']
        verbose_name_plural = "Attendances"
        ordering = ['-date', '-marked_at']
    
    def __str__(self):
        return f"{self.student.username} - {self.subject.code} - {self.date}"