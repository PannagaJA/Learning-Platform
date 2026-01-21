# 🎯 GAMIFIED LEARNING SYSTEM - BACKEND DOCUMENTATION

## 📋 TABLE OF CONTENTS
- [System Overview](#system-overview)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Authentication & Authorization](#authentication--authorization)
- [Core Models](#core-models)
- [API Endpoints](#api-endpoints)
- [Admin Module APIs](#admin-module-apis)
- [HOD Module APIs](#hod-module-apis)
- [Faculty Module APIs](#faculty-module-apis)
- [Student Module APIs](#student-module-apis)
- [Common APIs](#common-apis)
- [Middleware](#middleware)
- [Permissions](#permissions)
- [Utilities](#utilities)

## 🏗️ SYSTEM OVERVIEW

The backend is built using Django with Python, implementing a RESTful API architecture. It manages user authentication, role-based access control, academic data, and all business logic for the role-based academic management system.

## 🛠️ TECHNOLOGY STACK

- **Framework**: Django 4.x with Python 3.9+
- **Web API**: Django REST Framework (DRF)
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: PostgreSQL
- **ORM**: Django ORM
- **Serialization**: DRF Serializers
- **Permissions**: Custom permission classes
- **Validation**: DRF validators and custom validators
- **CORS**: django-cors-headers
- **Environment**: python-decouple

## 📁 PROJECT STRUCTURE

```
backend/
├── backend/              # Django project settings
│   ├── __init__.py
│   ├── settings.py       # Configuration settings
│   ├── urls.py          # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
├── users/               # User management app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py        # User models
│   ├── views.py         # User API views
│   ├── serializers.py   # User serializers
│   ├── urls.py          # User URLs
│   ├── permissions.py   # Custom permissions
│   └── migrations/      # Database migrations
├── admin_app/           # Admin-specific functionality
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── faculty_app/         # Faculty-specific functionality
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── student_app/         # Student-specific functionality
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── api_documentation.md # API documentation
├── requirements.txt     # Dependencies
└── manage.py           # Django management script
```

## 🗄️ DATABASE SCHEMA

### 1. User Model (Extended AbstractUser)
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `username` (CharField) - Unique username
- `email` (EmailField) - User email address
- `first_name` (CharField) - First name
- `last_name` (CharField) - Last name
- `role` (CharField) - User role ('admin', 'hod', 'faculty', 'student')
- `department` (ForeignKey) - Associated department (nullable for students)
- `semester` (ForeignKey) - Associated semester (for students)
- `section` (ForeignKey) - Associated section (for students)
- `is_active` (BooleanField) - Account active status
- `date_joined` (DateTimeField) - Account creation date
- `last_login` (DateTimeField) - Last login timestamp

### 2. Department Model
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `name` (CharField) - Department name (unique)
- `code` (CharField) - Department code (unique)
- `hod` (ForeignKey) - Head of Department (nullable)
- `created_at` (DateTimeField) - Creation timestamp
- `updated_at` (DateTimeField) - Update timestamp

### 3. Semester Model
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `number` (IntegerField) - Semester number (1-8)
- `academic_year` (CharField) - Academic year (e.g., "2023-24")
- `department` (ForeignKey) - Associated department
- `is_active` (BooleanField) - Active status
- `created_at` (DateTimeField) - Creation timestamp

### 4. Section Model
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `name` (CharField) - Section name (A, B, C)
- `semester` (ForeignKey) - Associated semester
- `faculty_incharge` (ForeignKey) - Faculty in charge (nullable)
- `student_count` (IntegerField) - Number of students
- `created_at` (DateTimeField) - Creation timestamp

### 5. Subject Model
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `name` (CharField) - Subject name
- `code` (CharField) - Subject code
- `credits` (IntegerField) - Credit hours
- `semester` (ForeignKey) - Associated semester
- `department` (ForeignKey) - Associated department
- `faculty_assigned` (ForeignKey) - Assigned faculty
- `created_at` (DateTimeField) - Creation timestamp

### 6. Attendance Model
**Location**: `faculty_app/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `student` (ForeignKey) - Associated student
- `subject` (ForeignKey) - Associated subject
- `date` (DateField) - Attendance date
- `status` (CharField) - Attendance status ('present', 'absent', 'late')
- `marked_by` (ForeignKey) - Faculty who marked attendance
- `created_at` (DateTimeField) - Creation timestamp
- `updated_at` (DateTimeField) - Update timestamp

### 7. Notification Model
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `title` (CharField) - Notification title
- `message` (TextField) - Notification content
- `sender` (ForeignKey) - User sending notification
- `recipient_role` (CharField) - Target role ('admin', 'hod', 'faculty', 'student')
- `department` (ForeignKey) - Target department (nullable)
- `is_read` (BooleanField) - Read status
- `sent_at` (DateTimeField) - Sent timestamp
- `expires_at` (DateTimeField) - Expiration timestamp

### 8. AuditLog Model
**Location**: `users/models.py`

**Fields**:
- `id` (AutoField) - Primary key
- `user` (ForeignKey) - User who performed action
- `action` (CharField) - Action performed
- `resource_type` (CharField) - Type of resource affected
- `resource_id` (IntegerField) - ID of resource affected
- `timestamp` (DateTimeField) - When action occurred
- `ip_address` (GenericIPAddressField) - IP address of request
- `details` (TextField) - Additional details about action

## 🔐 AUTHENTICATION & AUTHORIZATION

### JWT Authentication Setup
**Location**: `backend/settings.py`

**Configuration**:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT Settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}
```

### Custom Permission Classes
**Location**: `users/permissions.py`

**Classes**:
- `IsAdminUser` - Allows access only to admin users
- `IsHODUser` - Allows access only to HOD users
- `IsFacultyUser` - Allows access only to faculty users
- `IsStudentUser` - Allows access only to student users
- `IsSameDepartment` - Checks if user belongs to same department
- `CanModifyUser` - Controls user modification permissions

## 🏗️ CORE MODELS

### User Model Implementation
**Location**: `users/models.py`

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
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
        return f"{self.username} ({self.role})"
```

### Department Model Implementation
**Location**: `users/models.py`

```python
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    hod = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, 
                          limit_choices_to={'role': 'hod'})
    
    def __str__(self):
        return self.name
```

## 🌐 API ENDPOINTS

### Base URL
All API endpoints are prefixed with `/api/v1/`

### Authentication Endpoints

#### 1. Login
- **Endpoint**: `POST /auth/login/`
- **Description**: Authenticate user and return JWT tokens
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access": "string",
    "refresh": "string",
    "user": {
      "id": integer,
      "username": "string",
      "email": "string",
      "role": "string",
      "department": "string",
      "full_name": "string"
    }
  }
  ```

#### 2. Refresh Token
- **Endpoint**: `POST /auth/token/refresh/`
- **Description**: Refresh access token using refresh token
- **Request Body**:
  ```json
  {
    "refresh": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access": "string"
  }
  ```

#### 3. Logout
- **Endpoint**: `POST /auth/logout/`
- **Description**: Blacklist refresh token
- **Request Body**:
  ```json
  {
    "refresh": "string"
  }
  ```
- **Response**: `204 No Content`

## 👑 ADMIN MODULE APIS

### 1. User Management Endpoints

#### List All Users
- **Endpoint**: `GET /admin/users/`
- **Permission**: Admin only
- **Query Parameters**:
  - `role` (optional): Filter by role
  - `department` (optional): Filter by department
  - `page` (optional): Pagination page
- **Response**:
  ```json
  {
    "count": integer,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": integer,
        "username": "string",
        "email": "string",
        "role": "string",
        "department": "string",
        "is_active": boolean,
        "date_joined": "datetime"
      }
    ]
  }
  ```

#### Create User
- **Endpoint**: `POST /admin/users/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "first_name": "string",
    "last_name": "string",
    "role": "string",
    "department": integer (optional),
    "semester": integer (for students),
    "section": integer (for students)
  }
  ```
- **Response**: Created user object with 201 status

#### Update User
- **Endpoint**: `PUT /admin/users/{id}/`
- **Permission**: Admin only
- **Request Body**: Same as create but partial updates allowed
- **Response**: Updated user object

#### Delete User
- **Endpoint**: `DELETE /admin/users/{id}/`
- **Permission**: Admin only
- **Response**: 204 No Content

#### Assign Role
- **Endpoint**: `PATCH /admin/users/{id}/assign-role/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "role": "string",
    "department": integer (optional)
  }
  ```
- **Response**: Updated user object

#### Reset Password
- **Endpoint**: `POST /admin/users/{id}/reset-password/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "password": "string"
  }
  ```
- **Response**: Success message

### 2. Department Management Endpoints

#### List Departments
- **Endpoint**: `GET /admin/departments/`
- **Permission**: Admin only
- **Response**: Array of department objects

#### Create Department
- **Endpoint**: `POST /admin/departments/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "name": "string",
    "code": "string",
    "hod": integer (user id, optional)
  }
  ```
- **Response**: Created department object

#### Update Department
- **Endpoint**: `PUT /admin/departments/{id}/`
- **Permission**: Admin only
- **Response**: Updated department object

#### Delete Department
- **Endpoint**: `DELETE /admin/departments/{id}/`
- **Permission**: Admin only
- **Response**: 204 No Content

#### Assign HOD to Department
- **Endpoint**: `PATCH /admin/departments/{id}/assign-hod/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "hod_id": integer
  }
  ```
- **Response**: Updated department object

### 3. Academic Configuration Endpoints

#### List Semesters
- **Endpoint**: `GET /admin/semesters/`
- **Permission**: Admin only
- **Response**: Array of semester objects

#### Create Semester
- **Endpoint**: `POST /admin/semesters/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "number": integer,
    "academic_year": "string",
    "department": integer
  }
  ```
- **Response**: Created semester object

#### List Sections
- **Endpoint**: `GET /admin/sections/`
- **Permission**: Admin only
- **Response**: Array of section objects

#### Create Section
- **Endpoint**: `POST /admin/sections/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "name": "string",
    "semester": integer,
    "faculty_incharge": integer (optional)
  }
  ```
- **Response**: Created section object

#### List Subjects
- **Endpoint**: `GET /admin/subjects/`
- **Permission**: Admin only
- **Response**: Array of subject objects

#### Create Subject
- **Endpoint**: `POST /admin/subjects/`
- **Permission**: Admin only
- **Request Body**:
  ```json
  {
    "name": "string",
    "code": "string",
    "credits": integer,
    "semester": integer,
    "department": integer,
    "faculty_assigned": integer
  }
  ```
- **Response**: Created subject object

### 4. System Monitoring Endpoints

#### System Statistics
- **Endpoint**: `GET /admin/system-stats/`
- **Permission**: Admin only
- **Response**:
  ```json
  {
    "total_users": integer,
    "active_users": integer,
    "departments": integer,
    "recent_signups": integer
  }
  ```

#### Audit Logs
- **Endpoint**: `GET /admin/audit-logs/`
- **Permission**: Admin only
- **Query Parameters**:
  - `user_id` (optional): Filter by user
  - `action` (optional): Filter by action type
  - `date_from` (optional): Filter from date
  - `date_to` (optional): Filter to date
- **Response**: Array of audit log entries

## 🏫 HOD MODULE APIS

### 1. Faculty Management Endpoints

#### List Faculty in Department
- **Endpoint**: `GET /hod/faculty/`
- **Permission**: HOD only (same department)
- **Response**: Array of faculty objects in the HOD's department

#### Assign Subject to Faculty
- **Endpoint**: `POST /hod/faculty/{id}/assign-subject/`
- **Permission**: HOD only (same department)
- **Request Body**:
  ```json
  {
    "subject_id": integer
  }
  ```
- **Response**: Success message with updated faculty details

#### Monitor Faculty Workload
- **Endpoint**: `GET /hod/faculty-workload/`
- **Permission**: HOD only (same department)
- **Response**: Array of faculty with workload statistics

### 2. Student Monitoring Endpoints

#### List Students in Department
- **Endpoint**: `GET /hod/students/`
- **Permission**: HOD only (same department)
- **Query Parameters**:
  - `semester` (optional): Filter by semester
  - `section` (optional): Filter by section
- **Response**: Array of student objects in the department

#### Student Attendance Summary
- **Endpoint**: `GET /hod/student-attendance-summary/`
- **Permission**: HOD only (same department)
- **Query Parameters**:
  - `semester` (optional)
  - `section` (optional)
- **Response**: Attendance statistics for students

### 3. Attendance Overview Endpoints

#### Daily Attendance Summary
- **Endpoint**: `GET /hod/daily-attendance/`
- **Permission**: HOD only (same department)
- **Query Parameters**:
  - `date` (optional, defaults to today)
- **Response**: Daily attendance summary for the department

#### Section-wise Analytics
- **Endpoint**: `GET /hod/section-analytics/`
- **Permission**: HOD only (same department)
- **Response**: Analytics grouped by section

#### Low Attendance Alerts
- **Endpoint**: `GET /hod/low-attendance-alerts/`
- **Permission**: HOD only (same department)
- **Response**: List of students with low attendance

### 4. Notification Endpoints

#### Send Notification
- **Endpoint**: `POST /hod/notifications/`
- **Permission**: HOD only
- **Request Body**:
  ```json
  {
    "title": "string",
    "message": "string",
    "recipient_role": "string",
    "department": integer (optional, for targeted notifications)
  }
  ```
- **Response**: Created notification object

#### List Notifications
- **Endpoint**: `GET /hod/notifications/`
- **Permission**: HOD only
- **Response**: Array of notifications sent by the HOD

### 5. Report Generation Endpoints

#### Export Attendance (CSV)
- **Endpoint**: `GET /hod/export-attendance-csv/`
- **Permission**: HOD only (same department)
- **Query Parameters**:
  - `semester` (optional)
  - `section` (optional)
  - `date_from` (optional)
  - `date_to` (optional)
- **Response**: CSV file download

#### Semester Reports
- **Endpoint**: `GET /hod/semester-reports/`
- **Permission**: HOD only (same department)
- **Query Parameters**:
  - `semester_id`: Integer
- **Response**: Detailed semester report

#### Faculty Performance Reports
- **Endpoint**: `GET /hod/faculty-performance-reports/`
- **Permission**: HOD only (same department)
- **Response**: Performance metrics for faculty in department

## 👨‍🏫 FACULTY MODULE APIS

### 1. Class Dashboard Endpoints

#### My Classes
- **Endpoint**: `GET /faculty/my-classes/`
- **Permission**: Faculty only
- **Response**: Array of classes assigned to the faculty

#### Class Details
- **Endpoint**: `GET /faculty/classes/{id}/`
- **Permission**: Faculty only (own class)
- **Response**: Detailed class information with student list

### 2. Attendance Management Endpoints

#### Mark Attendance
- **Endpoint**: `POST /faculty/mark-attendance/`
- **Permission**: Faculty only
- **Request Body**:
  ```json
  {
    "subject_id": integer,
    "date": "date",
    "attendance_data": [
      {
        "student_id": integer,
        "status": "present/absent/late"
      }
    ]
  }
  ```
- **Response**: Success confirmation with attendance records

#### Get Attendance Session
- **Endpoint**: `GET /faculty/attendance-session/`
- **Permission**: Faculty only
- **Query Parameters**:
  - `subject_id`: Integer
  - `date`: Date (optional, defaults to today)
- **Response**: Existing attendance session or template

#### Edit Attendance
- **Endpoint**: `PUT /faculty/attendance/{id}/`
- **Permission**: Faculty only (own attendance records)
- **Request Body**: Updated attendance data
- **Response**: Updated attendance record

#### Attendance Summary
- **Endpoint**: `GET /faculty/attendance-summary/`
- **Permission**: Faculty only
- **Query Parameters**:
  - `subject_id` (optional)
  - `date_range` (optional)
- **Response**: Attendance summary for faculty's classes

### 3. Student Communication Endpoints

#### Student List for Class
- **Endpoint**: `GET /faculty/class-students/{subject_id}/`
- **Permission**: Faculty only (own subject)
- **Response**: List of students enrolled in the faculty's subject

#### Send Class Announcement
- **Endpoint**: `POST /faculty/send-announcement/`
- **Permission**: Faculty only
- **Request Body**:
  ```json
  {
    "subject_id": integer,
    "title": "string",
    "message": "string"
  }
  ```
- **Response**: Created announcement notification

### 4. Report Generation Endpoints

#### Subject-wise Attendance Report
- **Endpoint**: `GET /faculty/subject-attendance-report/{subject_id}/`
- **Permission**: Faculty only (own subject)
- **Response**: Detailed attendance report for the subject

#### Individual Student Report
- **Endpoint**: `GET /faculty/student-report/{student_id}/`
- **Permission**: Faculty only (students in own classes)
- **Response**: Detailed report for the specific student

## 🎓 STUDENT MODULE APIS

### 1. Profile Management Endpoints

#### Get Profile
- **Endpoint**: `GET /student/profile/`
- **Permission**: Student only (own profile)
- **Response**:
  ```json
  {
    "id": integer,
    "username": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "department": "string",
    "semester": "string",
    "section": "string"
  }
  ```

#### Update Profile
- **Endpoint**: `PUT /student/profile/`
- **Permission**: Student only (own profile)
- **Request Body**: Partial profile updates
- **Response**: Updated profile

### 2. Attendance View Endpoints

#### My Attendance
- **Endpoint**: `GET /student/my-attendance/`
- **Permission**: Student only (own attendance)
- **Query Parameters**:
  - `subject_id` (optional): Filter by subject
  - `month` (optional): Filter by month
- **Response**: Array of attendance records

#### Monthly Summary
- **Endpoint**: `GET /student/monthly-attendance-summary/`
- **Permission**: Student only (own data)
- **Query Parameters**:
  - `month`: Integer (1-12)
  - `year`: Integer
- **Response**: Monthly attendance summary

#### Eligibility Status
- **Endpoint**: `GET /student/eligibility-status/`
- **Permission**: Student only (own data)
- **Response**: Eligibility status based on attendance

### 3. Notification Endpoints

#### Get Notifications
- **Endpoint**: `GET /student/notifications/`
- **Permission**: Student only
- **Query Parameters**:
  - `unread_only` (optional): Boolean
- **Response**: Array of notifications for the student

#### Mark Notification Read
- **Endpoint**: `PATCH /student/notifications/{id}/mark-read/`
- **Permission**: Student only (own notifications)
- **Response**: Success confirmation

### 4. Support & Query Endpoints

#### Submit Query
- **Endpoint**: `POST /student/submit-query/`
- **Permission**: Student only
- **Request Body**:
  ```json
  {
    "subject": "string",
    "message": "string",
    "category": "attendance/academic/other"
  }
  ```
- **Response**: Created query ticket

#### Contact Faculty
- **Endpoint**: `POST /student/contact-faculty/`
- **Permission**: Student only
- **Request Body**:
  ```json
  {
    "faculty_id": integer,
    "message": "string"
  }
  ```
- **Response**: Message sent confirmation

## 🔁 COMMON APIS

### 1. Notification Endpoints (Available to all roles)

#### Get User Notifications
- **Endpoint**: `GET /notifications/`
- **Permission**: Authenticated user
- **Query Parameters**:
  - `unread_only` (optional)
  - `limit` (optional)
- **Response**: Array of user's notifications

#### Mark All Read
- **Endpoint**: `POST /notifications/mark-all-read/`
- **Permission**: Authenticated user
- **Response**: Success confirmation

### 2. Search & Filter Endpoints

#### Global Search
- **Endpoint**: `GET /search/`
- **Permission**: Authenticated user
- **Query Parameters**:
  - `q`: Search query
  - `type`: Resource type to search (users/departments/subjects)
- **Response**: Search results based on type and permissions

### 3. File Upload Endpoints

#### Upload Document
- **Endpoint**: `POST /upload/document/`
- **Permission**: Based on context
- **Form Data**:
  - `file`: File to upload
  - `purpose`: Purpose of upload
- **Response**: File upload confirmation with URL

## 🛡️ MIDDLEWARE

### 1. JWT Authentication Middleware
**Location**: Custom JWT authentication using DRF's built-in support

Handles token validation and user authentication for protected endpoints.

### 2. Role-Based Access Middleware
**Location**: `users/middleware.py`

Custom middleware that checks user roles and permissions for specific endpoints.

### 3. Audit Logging Middleware
**Location**: `users/middleware.py`

Automatically logs important user actions for auditing purposes.

## 🔐 PERMISSIONS

### Custom Permission Classes

#### IsAdminUser
Ensures only users with 'admin' role can access the endpoint.

#### IsHODUser
Ensures only users with 'hod' role can access the endpoint.

#### IsFacultyUser
Ensures only users with 'faculty' role can access the endpoint.

#### IsStudentUser
Ensures only users with 'student' role can access the endpoint.

#### IsSameDepartment
Checks if requesting user belongs to the same department as the resource.

#### CanModifyUser
Controls which users can modify other user accounts based on role hierarchy.

## 🛠️ UTILITIES

### 1. Helper Functions
**Location**: `users/utils.py`

- `generate_unique_username(email)` - Generates unique username from email
- `send_notification_email(notification)` - Sends email notifications
- `calculate_attendance_percentage(student_id, subject_id)` - Calculates attendance percentage
- `validate_academic_structure()` - Validates academic data relationships

### 2. Serializers
**Location**: Various apps' `serializers.py` files

Custom serializers for all models with appropriate validation and nested representations.

### 3. Pagination Classes
**Location**: `users/pagination.py`

Custom pagination classes for API responses with configurable page sizes.

### 4. Exception Handlers
**Location**: `users/exceptions.py`

Custom exception classes and handlers for specific business logic errors.

---

This backend documentation provides a comprehensive guide for implementing the server-side functionality of the role-based academic management system. Each API endpoint is documented with request/response formats, permissions, and usage examples.