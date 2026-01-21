# Learning Platform - Academic Management System

This is a comprehensive role-based academic management system built with Django REST Framework backend and React/Vite TypeScript frontend.

## 🚀 Features

- Role-based access control (Admin, HOD, Faculty, Student)
- Academic management (Departments, Semesters, Sections, Subjects)
- Attendance tracking and analytics
- Notification system
- User management
- Responsive web design with modern UI

## 🛠️ Tech Stack

- **Backend**: Django 4.2+, Django REST Framework, JWT Authentication
- **Frontend**: React 18+, TypeScript, Vite, Tailwind CSS
- **Database**: SQLite (default), PostgreSQL (production)
- **State Management**: Zustand
- **API Client**: Axios

## 📋 Prerequisites

- Python 3.12+
- Node.js 18+
- npm or yarn
- conda (recommended)

## 🚀 Quick Setup

### Option 1: Using Conda (Recommended)

1. Create and activate the conda environment:
   ```bash
   conda create -n learning python=3.12
   conda activate learning
   ```

2. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the backend server:
   ```bash
   python manage.py runserver
   ```

6. In a new terminal, navigate to the frontend directory:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### Option 2: Using Virtual Environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Follow steps 2-6 from Option 1.

## 🏗️ Project Structure

```
backend/          # Django REST API
├── users/         # User management app
├── admin_app/     # Admin module
├── faculty_app/   # Faculty module
├── student_app/   # Student module
frontend/         # React/Vite frontend
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── store/
│   └── styles/
```

## 🌐 API Endpoints

- Base URL: `http://localhost:8000/api/v1/`
- Authentication: `POST /auth/login/`
- Users: `GET/POST /users/`
- Admin: `GET/POST /admin/`
- HOD: `GET/POST /hod/`
- Faculty: `GET/POST /faculty/`
- Student: `GET/POST /student/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.