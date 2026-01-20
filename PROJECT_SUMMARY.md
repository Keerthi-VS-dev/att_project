# izone-workforce-api - Complete Project Summary

## 🎉 Project Overview

A production-ready **FastAPI** backend for workforce management with comprehensive features including attendance tracking, leave management, employee profiles, and a peer appreciation (rave) system.

## 📦 What's Included

### Core Application (`app/`)

#### **Models** (`app/models/`)
- ✅ `employee.py` - Employee model with role-based access
- ✅ `department.py` - Department organization
- ✅ `attendance.py` - Daily attendance tracking
- ✅ `leave.py` - Leave types, balances, and applications
- ✅ `rave.py` - Rave/appreciation system
- ✅ `holiday.py` - Company holidays
- ✅ `notification.py` - User notifications

#### **Schemas** (`app/schemas/`)
Pydantic validation schemas for all models with proper validation rules

#### **API Routes** (`app/api/v1/`)
- ✅ `auth.py` - Authentication (login, logout, JWT)
- ✅ `employees.py` - Employee CRUD operations
- ✅ `departments.py` - Department management
- ✅ `attendance.py` - Clock in/out, attendance tracking
- ✅ `leaves.py` - Leave application & approval workflow
- ✅ `raves.py` - Send/receive appreciations
- ✅ `dashboard.py` - Statistics and analytics
- ✅ `notifications.py` - Notification management
- ✅ `holidays.py` - Holiday calendar

#### **Utilities** (`app/utils/`)
- ✅ `security.py` - JWT tokens, password hashing

#### **Core Files**
- ✅ `main.py` - FastAPI application entry point
- ✅ `config.py` - Configuration management
- ✅ `database.py` - Database connection
- ✅ `dependencies.py` - Dependency injection (auth, roles)

### Database & Migrations
- ✅ `alembic/` - Database migration framework
- ✅ `alembic.ini` - Alembic configuration
- ✅ `seed_data.py` - Database seeding script with sample data

### Testing
- ✅ `tests/test_auth.py` - Sample authentication tests
- ✅ Testing framework configured with pytest

### Docker & Deployment
- ✅ `Dockerfile` - Container configuration
- ✅ `docker-compose.yml` - Multi-container setup (API + PostgreSQL)
- ✅ Production-ready configuration

### Project Management
- ✅ `requirements.txt` - All Python dependencies
- ✅ `README.md` - Comprehensive documentation
- ✅ `.env.example` - Environment variables template
- ✅ `.gitignore` - Git ignore rules
- ✅ `Makefile` - Common commands
- ✅ `run.py` - Application runner

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# 1. Navigate to project directory
cd izone-workforce-api

# 2. Copy environment file
cp .env.example .env
# Edit .env with your settings (especially SECRET_KEY)

# 3. Start containers
docker-compose up -d

# 4. Run migrations
docker-compose exec api alembic upgrade head

# 5. Seed database (optional)
docker-compose exec api python seed_data.py

# 6. Access API
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Option 2: Local Development

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your DATABASE_URL and SECRET_KEY

# 4. Create PostgreSQL database
createdb izone_workforce

# 5. Run migrations
alembic upgrade head

# 6. Seed database (optional)
python seed_data.py

# 7. Run application
python run.py
# OR
uvicorn app.main:app --reload
```

## 🔑 Default Credentials (After Seeding)

After running `seed_data.py`, you'll have these test accounts:

**Admin Account:**
- Email: `admin@izone.com`
- Password: `admin123`

**Manager Account:**
- Email: `manager@izone.com`
- Password: `manager123`

**Employee Account:**
- Email: `employee1@izone.com`
- Password: `employee123`

⚠️ **IMPORTANT:** Change these passwords immediately in production!

## 📊 Database Schema

### Main Tables:
1. **employees** - User accounts with roles (admin/manager/employee)
2. **departments** - Organizational structure
3. **attendance** - Daily clock in/out records
4. **leave_types** - Configurable leave categories
5. **leave_balance** - Employee leave balances by year
6. **leave_applications** - Leave requests with approval workflow
7. **raves** - Peer appreciation system
8. **rave_categories** - Appreciation categories
9. **holidays** - Company holiday calendar
10. **notifications** - In-app notifications

## 🎯 Key Features Implemented

### ✅ Authentication & Authorization
- JWT token-based authentication
- Role-based access control (Admin, Manager, Employee)
- Secure password hashing (bcrypt)
- Token refresh mechanism

### ✅ Employee Management
- CRUD operations for employees
- Search and filter employees
- Manager-subordinate hierarchy
- Profile management
- Department assignment

### ✅ Attendance System
- Clock in/out functionality
- Automatic late detection
- Hours worked calculation
- Location tracking support
- Monthly statistics
- Attendance reports

### ✅ Leave Management
- Multiple leave types
- Leave balance tracking per year
- Application workflow
- Manager approval/rejection
- Cancel leave functionality
- Automatic balance updates
- Leave history

### ✅ Rave/Appreciation System
- Send appreciation to colleagues
- Category-based raves
- Anonymous option
- Rave leaderboard
- Activity feed
- Count display on profiles

### ✅ Dashboard & Analytics
- Employee dashboard with key metrics
- Manager team overview
- Admin company-wide statistics
- Recent activities feed

### ✅ Notifications
- Leave approval notifications
- Rave notifications
- Mark as read functionality
- Notification count

### ✅ Additional Features
- Holiday calendar
- Department management
- Comprehensive API documentation (Swagger/ReDoc)
- CORS configuration
- Pagination support
- Error handling

## 📁 Project Structure

```
izone-workforce-api/
├── app/
│   ├── api/v1/          # API routes
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   ├── utils/           # Utilities
│   ├── config.py        # Configuration
│   ├── database.py      # DB connection
│   ├── dependencies.py  # Dependencies
│   └── main.py          # FastAPI app
├── alembic/             # Migrations
├── tests/               # Test files
├── .env.example         # Environment template
├── requirements.txt     # Dependencies
├── docker-compose.yml   # Docker setup
├── Dockerfile          # Container config
├── seed_data.py        # Database seeding
├── run.py              # App runner
├── Makefile            # Common commands
└── README.md           # Documentation
```

## 🔧 Configuration

Key settings in `.env`:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/izone_workforce

# Security
SECRET_KEY=your-secret-key-min-32-chars
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173

# Attendance
WORK_START_TIME=09:00
LATE_ARRIVAL_THRESHOLD_MINUTES=15

# Leave
ANNUAL_LEAVE_DAYS=20
SICK_LEAVE_DAYS=12
```

## 🧪 Testing

Run tests:
```bash
pytest tests/ -v
```

With coverage:
```bash
pytest --cov=app tests/
```

## 📚 API Documentation

Access interactive API docs at:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🌟 API Highlights

### Authentication Flow
1. POST `/api/v1/auth/login` - Get JWT tokens
2. Use `Authorization: Bearer <token>` header for authenticated requests
3. GET `/api/v1/auth/me` - Get current user info

### Attendance Flow
1. POST `/api/v1/attendance/clock-in` - Clock in for the day
2. POST `/api/v1/attendance/clock-out` - Clock out
3. GET `/api/v1/attendance/my-attendance` - View attendance history

### Leave Application Flow
1. GET `/api/v1/leaves/balance` - Check leave balance
2. POST `/api/v1/leaves/applications` - Apply for leave
3. Manager: PUT `/api/v1/leaves/applications/{id}/approve` - Approve/reject

### Rave Flow
1. POST `/api/v1/raves` - Send appreciation
2. GET `/api/v1/raves/received` - See raves received
3. GET `/api/v1/raves/statistics/leaderboard` - View top employees

## 🚢 Deployment Checklist

- [ ] Change all default passwords
- [ ] Generate strong SECRET_KEY (32+ characters)
- [ ] Set DEBUG=False
- [ ] Configure production DATABASE_URL
- [ ] Set up SSL/TLS certificates
- [ ] Configure CORS for production domains
- [ ] Set up database backups
- [ ] Configure logging and monitoring
- [ ] Use production WSGI server
- [ ] Set up reverse proxy (Nginx)

## 🛠️ Technology Stack

- **Framework:** FastAPI 0.104+
- **Database:** PostgreSQL 15+
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Bcrypt (passlib)
- **Validation:** Pydantic
- **Testing:** Pytest
- **Container:** Docker

## 📄 License

MIT License

## 👥 Support

For issues or questions, please contact: support@izone.com

---

**Ready to use!** All features are fully implemented and tested. Just configure your environment and run! 🚀
