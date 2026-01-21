# 🎯 GAMIFIED LEARNING SYSTEM - FRONTEND DOCUMENTATION

<div class="gradient" style="background: linear-gradient(135deg, #e8e9ea, #e7e9fb); padding: 20px; border-radius: var(--radius-lg); margin-bottom: 20px;">

## 📋 TABLE OF CONTENTS
- [System Overview](#system-overview)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Theme System](#theme-system)
- [Authentication Pages](#authentication-pages)
- [Admin Module Pages](#admin-module-pages)
- [HOD Module Pages](#hod-module-pages)
- [Faculty Module Pages](#faculty-module-pages)
- [Student Module Pages](#student-module-pages)
- [Common Components](#common-components)
- [State Management](#state-management)
- [API Integration](#api-integration)
- [Responsive Design Guidelines](#responsive-design-guidelines)

</div>

## 🏗️ SYSTEM OVERVIEW

The frontend is built using React with Vite and TypeScript, following modern development practices. It implements a role-based access control system with different dashboards and functionalities for each user role (Admin, HOD, Faculty, Student). The application uses a comprehensive theme system based on Tailwind CSS with OKLCH color space for better accessibility and theming.

## 🛠️ TECHNOLOGY STACK

- **Framework**: React 18+ with TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS with custom theme system
- **UI Components**: Shadcn/ui components (New York style)
- **State Management**: Zustand
- **Routing**: React Router v6
- **API Calls**: Axios
- **Authentication**: JWT-based
- **Icons**: Lucide React
- **Animations**: Custom CSS animations (ripple, blob, loader)

## 📁 PROJECT STRUCTURE

```
src/
├── components/           # Reusable UI components
│   ├── auth/           # Authentication components
│   ├── admin/          # Admin-specific components
│   ├── hod/            # HOD-specific components
│   ├── faculty/        # Faculty-specific components
│   ├── student/        # Student-specific components
│   ├── common/         # Shared components
│   ├── ui/             # Base UI components (shadcn)
│   └── layout/         # Layout components
├── pages/              # Page components
│   ├── auth/           # Login/Register pages
│   ├── admin/          # Admin dashboard pages
│   ├── hod/            # HOD dashboard pages
│   ├── faculty/        # Faculty dashboard pages
│   ├── student/        # Student dashboard pages
│   └── shared/         # Shared pages
├── hooks/              # Custom React hooks
├── services/           # API services
├── store/              # State management stores
├── styles/             # Theme and styling files
│   ├── globals.css     # Global styles and theme variables
│   └── themes/         # Theme-specific files
├── types/              # TypeScript type definitions
├── lib/                # Utility functions
└── assets/             # Static assets
```

## 🎨 THEME SYSTEM

The application implements a comprehensive theme system using Tailwind CSS with OKLCH color space for better accessibility and theming. The theme supports both light and dark modes with smooth transitions.

### Color Palette

#### Custom Colors
- `--color-green: #b9ff66` - Primary accent color
- `--color-gray: #f3f3f3` - Light gray background
- `--color-dark: #191a23` - Dark text/background

#### Light Theme (Default)
Uses OKLCH color space for better accessibility:
- `--background: oklch(1 0 0)` - Pure white
- `--foreground: oklch(0.145 0 0)` - Near black text
- `--primary: oklch(0.205 0 0)` - Primary buttons
- `--secondary: oklch(0.97 0 0)` - Secondary elements

#### Dark Theme
- `--background: oklch(0.145 0 0)` - Dark background
- `--foreground: oklch(0.985 0 0)` - Light text
- `--primary: oklch(0.922 0 0)` - Light primary
- `--secondary: oklch(0.269 0 0)` - Dark secondary

### Typography

- **Fonts**: `--font-sans: var(--font-geist-sans)` and `--font-mono: var(--font-geist-mono)`
- **Border Radius**: `--radius: 0.625rem` (10px base) with variations (sm, md, lg, xl)

### Animations

- **Ripple Effect**: Two-layer ripple animation for interactive elements
- **Blob Animation**: Organic floating animation for decorative elements
- **Loader Animation**: Custom spinning loader
- **Carousel Animation**: Horizontal scrolling with Embla

### Component Styling

- **Buttons**: Primary buttons use `bg-[#CAC5FE]` with hover effects
- **Headers**: Styled with `bg-blue-200` and rounded corners
- **Layout**: Gradient backgrounds using `linear-gradient(135deg, #e8e9ea, #e7e9fb)`

### Accessibility Features

- OKLCH color space for better contrast ratios
- Proper focus states with `outline-ring/50`
- Semantic color naming for consistent meaning
- Dark mode support with automatic contrast adjustment

## 🔐 AUTHENTICATION PAGES

### 1. Login Page (`/login`)
**Component Path**: `src/pages/auth/Login.tsx`

**Purpose**: User authentication entry point for all roles

**Features**:
- Email/Username and password fields
- Form validation with error handling
- Loading states during authentication
- Forgot password link
- Social login options (optional)
- Remember me functionality

**UI Components**:
- Card wrapper with form (using theme-styled cards with `--radius-lg` border radius)
- Input fields with validation (following theme color palette)
- Submit button with loading spinner (styled with `primary-button` class using `bg-[#CAC5FE]`)
- Link to register page
- Error message display (using theme's destructive color `oklch(0.577 0.245 27.325)`)

**Props**:
- `onLoginSuccess`: Callback function after successful login

**State Management**:
- Handles form inputs and validation
- Manages authentication state
- Stores JWT token upon successful login

---

### 2. Registration Page (`/register`)
**Component Path**: `src/pages/auth/Register.tsx`

**Purpose**: User registration with role selection

**Features**:
- Email, username, password fields
- Role selection dropdown (Admin, HOD, Faculty, Student)
- Password confirmation
- Form validation
- Terms and conditions acceptance

**UI Components**:
- Multi-step registration form (with gradient background `linear-gradient(135deg, #e8e9ea, #e7e9fb)`)
- Role selection cards (themed with appropriate border radius and colors)
- Password strength indicator (using theme's color system)
- Terms checkbox (following theme styling)

**Props**:
- `onRegisterSuccess`: Callback after successful registration

---

## 👑 ADMIN MODULE PAGES

### 1. Admin Dashboard (`/admin/dashboard`)
**Component Path**: `src/pages/admin/AdminDashboard.tsx`

**Purpose**: Main administrative dashboard with system overview

**Features**:
- User statistics widgets
- System performance metrics
- Recent activity timeline
- Quick access buttons to key functions
- System health indicators

**UI Components**:
- Grid layout with themed cards (using `--radius-lg` border radius and theme colors)
- Chart components for analytics (using theme's chart colors: `--chart-1` to `--chart-5`)
- Activity feed (following theme's foreground and background colors)
- Statistic counters (themed with primary/secondary colors)
- Quick action buttons (styled with `primary-button` class)

**Data Requirements**:
- Total users count
- Active sessions
- Recent signups
- System notifications

---

### 2. User Management Page (`/admin/users`)
**Component Path**: `src/pages/admin/UserManagement.tsx`

**Purpose**: Create, edit, and manage all system users

**Features**:
- User listing with search/filter
- Add new user form
- Edit existing user details
- Role assignment interface
- Enable/disable user toggle
- Bulk operations
- User status indicators

**UI Components**:
- Data table with pagination (using theme's border and background colors)
- Modal forms for user operations (themed with appropriate radius and colors)
- Search and filter controls (following input styling with `--input` color)
- Status badges (using theme's accent and destructive colors)
- Action dropdown menus (using theme's popover styling)

**Form Fields**:
- First name, last name
- Email, username
- Role selection
- Department assignment
- Status toggle

---

### 3. Department Management (`/admin/departments`)
**Component Path**: `src/pages/admin/DepartmentManagement.tsx`

**Purpose**: Create and manage academic departments

**Features**:
- Department listing
- Add/edit department form
- HOD assignment interface
- Department statistics
- Active/inactive toggle

**UI Components**:
- Department cards (using theme's card styling with `--radius-lg`)
- Modal for department operations (following theme's popover design)
- Assignment dropdowns (using theme's select/input styling)
- Status indicators (using theme's color system for different states)

---

### 4. Academic Configuration (`/admin/academics`)
**Component Path**: `src/pages/admin/AcademicConfiguration.tsx`

**Purpose**: Configure semesters, sections, and subjects

**Features**:
- Semester management interface
- Section creation tools
- Subject assignment system
- Academic year configuration
- Curriculum mapping

**UI Components**:
- Tabbed interface for different entities (themed with theme's border and background colors)
- Form builders (using theme's input and button styles)
- Drag-and-drop assignment tools (with ripple animation effects)
- Academic calendar view (following theme's card and typography styles)

---

### 5. System Monitoring (`/admin/monitoring`)
**Component Path**: `src/pages/admin/SystemMonitoring.tsx`

**Purpose**: Monitor system usage and performance

**Features**:
- Platform usage analytics
- Audit log viewer
- Error tracking dashboard
- Performance metrics
- System health reports

**UI Components**:
- Charts and graphs (using theme's chart colors `--chart-1` to `--chart-5`)
- Log table with filters (following theme's table and input styles)
- Health indicators (using theme's status colors)
- Export functionality (with themed buttons and modal dialogs)

---

## 🏫 HOD MODULE PAGES

### 1. HOD Dashboard (`/hod/dashboard`)
**Component Path**: `src/pages/hod/HodDashboard.tsx`

**Purpose**: Department-level overview for HOD

**Features**:
- Department statistics
- Faculty performance overview
- Student enrollment metrics
- Attendance summary
- Upcoming events

**UI Components**:
- Department header with details (using themed header style with `blue-head` class)
- Statistic cards (using theme's card styling with appropriate colors)
- Performance charts (using theme's chart colors)
- Quick notification panel (following theme's popover design)

---

### 2. Faculty Management (`/hod/faculty`)
**Component Path**: `src/pages/hod/FacultyManagement.tsx`

**Purpose**: Manage faculty members in the department

**Features**:
- Faculty listing with details
- Subject assignment interface
- Workload monitoring
- Performance tracking
- Communication tools

**UI Components**:
- Faculty directory grid (using theme's grid and card styling)
- Assignment modal (themed with popover colors and `--radius-lg`)
- Workload indicators (using theme's chart and status colors)
- Performance badges (using theme's accent and primary colors)

---

### 3. Student Monitoring (`/hod/students`)
**Component Path**: `src/pages/hod/StudentMonitoring.tsx`

**Purpose**: Monitor students in the department

**Features**:
- Student listing with filtering
- Semester/section views
- Attendance tracking
- Performance analytics
- Alert system for issues

**UI Components**:
- Filterable student table (using theme's table and input styles)
- Attendance indicators (using theme's status colors and chart system)
- Performance graphs (using theme's chart colors)
- Alert banners (themed with destructive color for warnings)

---

### 4. Attendance Overview (`/hod/attendance`)
**Component Path**: `src/pages/hod/AttendanceOverview.tsx`

**Purpose**: View attendance analytics across department

**Features**:
- Daily attendance summary
- Section-wise analytics
- Low attendance alerts
- Trend analysis
- Export options

**UI Components**:
- Calendar view (using theme's card and background colors)
- Attendance charts (using theme's chart color system)
- Alert panels (using theme's destructive color for low attendance alerts)
- Export buttons (styled with theme's button variants)

---

### 5. Notification Center (`/hod/notifications`)
**Component Path**: `src/pages/hod/NotificationCenter.tsx`

**Purpose**: Create and send notifications

**Features**:
- Notification composer
- Target selection (faculty/students)
- Message templates
- Delivery tracking
- History view

**UI Components**:
- Rich text editor (using theme's input and border styling)
- Target selector (following theme's select component design)
- Preview panel (using themed card styling)
- History table (with theme's table colors and typography)

---

### 6. Reports & Export (`/hod/reports`)
**Component Path**: `src/pages/hod/Reports.tsx`

**Purpose**: Generate and export various reports

**Features**:
- Attendance reports
- Semester reports
- Faculty performance reports
- Export to CSV/PDF
- Scheduled reports

**UI Components**:
- Report type selector (using theme's select component styling)
- Date range pickers (following theme's input design)
- Export options (with themed button variants)
- Generated reports list (using theme's card and typography styles)

---

## 👨‍🏫 FACULTY MODULE PAGES

### 1. Faculty Dashboard (`/faculty/dashboard`)
**Component Path**: `src/pages/faculty/FacultyDashboard.tsx`

**Purpose**: Faculty member's main dashboard

**Features**:
- Assigned classes overview
- Today's schedule
- Pending attendance tasks
- Student messages
- Upcoming assignments

**UI Components**:
- Class summary cards (using theme's card styling with `--radius-lg`)
- Schedule calendar (with themed date picker design)
- Task counters (using theme's primary/secondary colors)
- Quick action buttons (styled with `primary-button` class)

---

### 2. Attendance Management (`/faculty/attendance`)
**Component Path**: `src/pages/faculty/AttendanceManagement.tsx`

**Purpose**: Mark and manage attendance for assigned classes

**Features**:
- Daily attendance marking
- Student roll call interface
- Attendance editing (restricted)
- Summary reports
- Session notes

**UI Components**:
- Student list with checkboxes (using theme's form element styling)
- Date pickers (following theme's input design)
- Status indicators (using theme's color system for attendance status)
- Summary panels (with themed card styling)

---

### 3. Class Dashboard (`/faculty/classes`)
**Component Path**: `src/pages/faculty/ClassDashboard.tsx`

**Purpose**: View and manage assigned classes

**Features**:
- Class listing with details
- Subject information
- Section schedules
- Class materials
- Student roster

**UI Components**:
- Class cards (using theme's card design with `--radius-lg`)
- Schedule tables (with theme's table styling)
- Material lists (following theme's list component design)
- Student count indicators (using theme's statistic styling)

---

### 4. Student Communication (`/faculty/communication`)
**Component Path**: `src/pages/faculty/StudentCommunication.tsx`

**Purpose**: Communicate with students in assigned classes

**Features**:
- Student directory
- Messaging interface
- Announcement creator
- Query responses
- Communication history

**UI Components**:
- Chat interface (using theme's background and border colors)
- Student list (with themed list styling)
- Message composer (following theme's input and button designs)
- History panels (using themed card components)

---

### 5. Reports (`/faculty/reports`)
**Component Path**: `src/pages/faculty/Reports.tsx`

**Purpose**: Generate subject-wise reports

**Features**:
- Subject-wise attendance reports
- Individual student reports
- Performance analytics
- Export options
- Comparison tools

**UI Components**:
- Report generators (using theme's form and card components)
- Chart displays (with theme's chart colors `--chart-1` to `--chart-5`)
- Export controls (themed with appropriate button variants)
- Filter options (using theme's select and input styles)

---

## 🎓 STUDENT MODULE PAGES

### 1. Student Dashboard (`/student/dashboard`)
**Component Path**: `src/pages/student/StudentDashboard.tsx`

**Purpose**: Student's personalized dashboard

**Features**:
- Personal profile summary
- Current semester details
- Attendance status
- Upcoming classes
- Recent notifications

**UI Components**:
- Profile card (using theme's card styling with `--radius-lg`)
- Semester information (following theme's typography)
- Attendance indicators (using theme's status colors)
- Schedule preview (with themed calendar design)
- Notification badge (using theme's accent color)

---

### 2. Profile Management (`/student/profile`)
**Component Path**: `src/pages/student/ProfileManagement.tsx`

**Purpose**: View and manage personal information

**Features**:
- Personal details view
- Department and section info
- Academic history
- Edit profile (limited)
- Privacy settings

**UI Components**:
- Profile card (using theme's card design with appropriate radius)
- Information display (following theme's typography and colors)
- Edit modals (themed with popover styling)
- Privacy toggles (using theme's form component design)

---

### 3. Attendance Viewer (`/student/attendance`)
**Component Path**: `src/pages/student/AttendanceViewer.tsx`

**Purpose**: View personal attendance records

**Features**:
- Subject-wise attendance
- Monthly summaries
- Eligibility status
- Attendance trends
- Download options

**UI Components**:
- Attendance table (using theme's table styling with border and background colors)
- Percentage indicators (with theme's status colors)
- Trend charts (using theme's chart color system)
- Download buttons (styled with theme's button variants)

---

### 4. Notification Center (`/student/notifications`)
**Component Path**: `src/pages/student/NotificationCenter.tsx`

**Purpose**: View received notifications and announcements

**Features**:
- Announcement listings
- Faculty messages
- Read/unread status
- Filtering options
- Notification preferences

**UI Components**:
- Notification cards (using theme's card styling with `--radius-lg`)
- Filter controls (following theme's input and button designs)
- Status indicators (using theme's color system for read/unread states)
- Preference settings (with themed form elements)

---

### 5. Support & Queries (`/student/support`)
**Component Path**: `src/pages/student/SupportQueries.tsx`

**Purpose**: Submit queries and raise issues

**Features**:
- Query submission form
- Issue reporting
- Faculty contact
- Support ticket tracking
- Response history

**UI Components**:
- Form builder (using theme's form components and styling)
- Ticket list (with themed card or table design)
- Contact interface (following theme's input and button styles)
- Response viewer (using theme's card and typography)

---

## 🔹 COMMON COMPONENTS

### 1. Navigation Sidebar
**Component Path**: `src/components/layout/Sidebar.tsx`

**Purpose**: Role-based navigation menu

**Features**:
- Dynamic menu based on user role (using themed navigation styling)
- Collapsible sections (with animated transitions)
- Active state highlighting (using theme's primary color)
- Icons for each section (following theme's iconography)
- Responsive behavior (with theme-aware breakpoints)

### 2. Top Navigation Bar
**Component Path**: `src/components/layout/TopNavbar.tsx`

**Purpose**: Top-level navigation and user controls

**Features**:
- User profile dropdown (themed with popover styling)
- Notification bell (using theme's accent color)
- Theme toggle (with smooth transition between light/dark modes)
- Search functionality (following theme's input design)
- Quick settings (using themed dropdown components)

### 3. Protected Route Component
**Component Path**: `src/components/layout/ProtectedRoute.tsx`

**Purpose**: Route protection based on authentication and roles

**Features**:
- Authentication check
- Role-based access control
- Redirect handling
- Loading states
- Error boundaries

### 4. Theme Provider
**Component Path**: `src/components/ui/theme-provider.tsx`

**Purpose**: Application-wide theme management

**Features**:
- Light/dark mode toggle (with smooth transitions using OKLCH color space)
- Theme persistence (storing preferences in localStorage)
- Context provider (using React Context API)
- System preference detection (auto-switching based on user's OS setting)

### 5. Toast/Alert System
**Component Path**: `src/components/ui/toast-system.tsx`

**Purpose**: Display notifications and alerts

**Features**:
- Success/error/info messages (using theme's color system: primary, destructive, etc.)
- Auto-dismissal (with customizable timing)
- Position management (top-right by default with theme-consistent styling)
- Stacking prevention (with theme-consistent spacing and radius)

## 🏪 STATE MANAGEMENT

### 1. Authentication Store
**File Path**: `src/store/authStore.ts`

**Purpose**: Manage authentication state globally

**State Properties**:
- `user`: Current user details
- `token`: JWT token
- `isLoading`: Authentication loading state
- `isLoggedIn`: Authentication status

**Actions**:
- `login`: Handle user login
- `logout`: Handle user logout
- `setUser`: Update user data
- `clearAuth`: Clear authentication data

### 2. User Management Store
**File Path**: `src/store/userStore.ts`

**Purpose**: Manage user-related state

**State Properties**:
- `users`: List of users
- `currentUser`: Currently viewed user
- `loading`: Loading states
- `filters`: Applied filters

**Actions**:
- `fetchUsers`: Get all users
- `createUser`: Create new user
- `updateUser`: Update existing user
- `deleteUser`: Delete user

### 3. Attendance Store
**File Path**: `src/store/attendanceStore.ts`

**Purpose**: Manage attendance-related state

**State Properties**:
- `attendanceRecords`: Attendance data
- `currentSession`: Active attendance session
- `loading`: Loading states

**Actions**:
- `markAttendance`: Mark attendance for session
- `getAttendance`: Fetch attendance data
- `updateAttendance`: Update attendance record

## 🌐 API INTEGRATION

### 1. API Service Layer
**File Path**: `src/services/api.ts`

**Purpose**: Centralized API client configuration

**Features**:
- Axios instance with interceptors
- Request/response transformers
- Error handling
- Token refresh logic
- Base URL configuration

### 2. Authentication Service
**File Path**: `src/services/authService.ts`

**Purpose**: Handle authentication-related API calls

**Methods**:
- `login(credentials)`
- `register(userData)`
- `logout()`
- `refreshToken()`
- `getCurrentUser()`

### 3. User Management Service
**File Path**: `src/services/userService.ts`

**Purpose**: Handle user-related API operations

**Methods**:
- `getAllUsers(filters)`
- `getUserById(id)`
- `createUser(userData)`
- `updateUser(id, userData)`
- `deleteUser(id)`

### 4. Attendance Service
**File Path**: `src/services/attendanceService.ts`

**Purpose**: Handle attendance-related API operations

**Methods**:
- `getAttendance(sessionId)`
- `markAttendance(attendanceData)`
- `getAttendanceReport(filters)`
- `updateAttendanceRecord(id, data)`

## 📱 RESPONSIVE DESIGN GUIDELINES

### Breakpoints
- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px+

### Responsive Patterns
1. **Navigation**: Sidebar collapses to hamburger menu on mobile
2. **Layout**: Cards stack vertically on smaller screens
3. **Forms**: Single column layout on mobile
4. **Tables**: Horizontal scrolling or card view on mobile
5. **Charts**: Simplified versions on smaller screens

### Touch-Friendly Elements
- Minimum 44px touch targets
- Adequate spacing between interactive elements
- Visual feedback for interactions
- Accessible color contrast ratios

## 🎨 DESIGN SYSTEM

### Color Palette
- **Primary**: Using `oklch(0.205 0 0)` for light mode and `oklch(0.922 0 0)` for dark mode (main actions)
- **Secondary**: Using `oklch(0.97 0 0)` for light mode and `oklch(0.269 0 0)` for dark mode (neutral elements)
- **Success**: Green for positive actions (using OKLCH color space)
- **Warning**: Yellow for warnings (using OKLCH color space)
- **Danger**: Red for errors and deletions (`oklch(0.577 0.245 27.325)`)
- **Info**: Indigo for informational elements (using OKLCH color space)
- **Chart Colors**: `--chart-1` to `--chart-5` using OKLCH values for consistent visualization

### Typography
- **Fonts**: Using Geist fonts as specified in theme (`--font-sans: var(--font-geist-sans)` and `--font-mono: var(--font-geist-mono)`)
- **Headers**: Following theme's typography scale
- **Body**: System font stack with theme-consistent sizing
- **Monospace**: For code and technical content using theme's monospace font
- **Line heights**: Optimized for readability according to theme

### Spacing System
- Based on theme's border radius system (`--radius: 0.625rem` with variations)
- Consistent padding and margin scales following theme's spacing system
- Harmonious proportional spacing using theme's design tokens

---

## 📊 WORKFLOW INTEGRATIONS

### Attendance Workflow
1. Faculty navigates to Attendance Management
2. Selects date and class
3. Marks attendance for students
4. System saves to database
5. HOD views analytics
6. Student sees summary on dashboard

### Notification Workflow
1. HOD/Admin opens Notification Center
2. Composes message
3. Selects target audience
4. Sends notification
5. Recipients receive in-app/email alerts
6. Delivery status tracked

---

This frontend documentation provides a comprehensive guide for implementing the role-based academic management system with all its pages, components, and features. Each section details the purpose, features, UI components, and technical requirements for every page in the system.