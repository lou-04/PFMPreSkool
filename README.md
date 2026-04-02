# PreSkool — Django School Management System

A complete school management web application built with Django, covering student management, staff management, scheduling, and examination tracking.

# link for the demonstration video :

https://youtu.be/qpIwrGMjBQk

## Features

| Module | Functionality |
|--------|--------------|
| **Authentication** | Login, signup, logout with role-based access (Admin / Teacher / Student) |
| **Dashboard** | Live stats: students, teachers, departments, subjects + upcoming holidays/exams |
| **Students** | Full CRUD with parent info (OneToOne relationship), photo upload |
| **Teachers** | Full CRUD with department assignment, photo upload |
| **Departments** | Create, edit, delete departments |
| **Subjects** | Link subjects to departments and teachers |
| **Holidays** | School holiday calendar |
| **Exams** | Schedule exams, enter and view results per student |
| **Time Table** | Weekly class schedule grouped by day |

## Installation

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd preskool

# 2. Create virtual environment
python -m venv monenv
monenv\Scripts\activate        # Windows
# source monenv/bin/activate   # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Load sample data (optional)
python manage.py loaddata fixtures/initial_data.json

# 6. Create superuser
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

Open http://localhost:8000 in your browser.

## Test Accounts

After running `createsuperuser`, log in at `/authentication/login/`.

To create role-based test accounts, visit `/authentication/signup/` and select a role (Student / Teacher / Admin).

| Role | Access |
|------|--------|
| Admin | Full access to all modules + Django admin panel |
| Teacher | Dashboard, students, timetable, exams |
| Student | Dashboard view |

## Project Structure

```
school/           ← Django project config (settings, main urls)
faculty/          ← Dashboard views
student/          ← Student + Parent models & CRUD
teacher/          ← Teacher model & CRUD
department/       ← Department model & CRUD
subject/          ← Subject model & CRUD
holiday/          ← Holiday calendar
exam/             ← Exam planning + result entry
timetable/        ← Weekly schedule
home_auth/        ← CustomUser model, login/signup/logout
templates/        ← All HTML templates (Bootstrap 5)
static/           ← Static assets
fixtures/         ← Sample data
```

## Tech Stack

- **Backend**: Django 6.0 (Python 3.13)
- **Database**: SQLite (default) — switchable to MySQL in `settings.py`
- **Frontend**: Bootstrap 5.3 (CDN), Bootstrap Icons
- **Auth**: Custom `AbstractUser` with role flags

## Database (MySQL option)

To switch to MySQL, update `DATABASES` in `school/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'preskool_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Then install: `pip install mysqlclient`
