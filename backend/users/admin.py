from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Department, Semester, Section, Subject, Notification, AuditLog, Attendance


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'department', 'semester', 'section', 'is_active', 'is_staff')


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'department', 'semester', 'section', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'department', 'semester', 'section', 'is_active', 'is_staff', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Academic Info', {'fields': ('role', 'department', 'semester', 'section')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'department', 'semester', 'section', 'is_active', 'is_staff'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'hod', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'code')
    ordering = ('name',)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('number', 'academic_year', 'created_at')
    list_filter = ('number', 'academic_year', 'created_at')
    ordering = ('academic_year', 'number')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'faculty_incharge', 'created_at')
    list_filter = ('semester', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits', 'semester', 'department', 'faculty_assigned', 'created_at')
    list_filter = ('semester', 'department', 'created_at')
    search_fields = ('name', 'code')
    ordering = ('name',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'sender', 'recipient_role', 'department', 'is_read', 'sent_at')
    list_filter = ('recipient_role', 'department', 'is_read', 'sent_at')
    search_fields = ('title', 'message')
    ordering = ('-sent_at',)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'resource_type', 'resource_id', 'timestamp', 'ip_address')
    list_filter = ('action', 'resource_type', 'timestamp', 'ip_address')
    search_fields = ('user__username', 'action', 'resource_type', 'resource_id')
    ordering = ('-timestamp',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'date', 'is_present', 'marked_by', 'marked_at')
    list_filter = ('is_present', 'date', 'subject', 'marked_at')
    search_fields = ('student__username', 'subject__name')
    ordering = ('-date',)


# Register the custom User model with the custom admin
admin.site.register(User, CustomUserAdmin)