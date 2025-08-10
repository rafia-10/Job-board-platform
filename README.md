JobBoard API

A RESTful API for managing job postings, categories, and applications. Built with Django, Django REST Framework, and PostgreSQL — optimized for fast job search using GIN indexes and pg_trgm extension.
Features

    Custom user roles: Admin and regular User

    CRUD for Job Categories — create categories first before posting jobs

    CRUD for Jobs with searchable fields: title, description, company, location

    Users can apply to jobs with resume upload and cover letter

    PostgreSQL full-text search optimized with GIN indexes and pg_trgm extension

Getting Started
Prerequisites

    Python 3.10+

    PostgreSQL database (with pg_trgm extension enabled)

    Git

Setup Instructions

    Clone the repo

git clone https://github.com/yourusername/jobboard.git
cd jobboard

    Create and activate a virtual environment

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

    Install dependencies

pip install -r requirements.txt

    Configure your database

    Create a PostgreSQL database

    Enable pg_trgm extension in your database (run in psql shell):

CREATE EXTENSION IF NOT EXISTS pg_trgm;

    Add your database URL in environment variables as DATABASE_URL

Example:

postgres://username:password@host:port/database_name

    Run migrations

python manage.py migrate

    Create a superuser (for admin access)

python manage.py createsuperuser

    Run the development server

python manage.py runserver

Usage Notes

    Important: You must create categories before posting any jobs — jobs require a category.

    Job search is optimized with PostgreSQL GIN indexes and trigram search for faster lookups.

    API endpoints (example):

Endpoint	Method	Description
/api/categories/	GET,POST	List & create categories
/api/jobs/	GET,POST	List & create jobs
/api/jobs/{id}/	GET,PUT,DELETE	Retrieve, update, delete a job
/api/applications/	GET,POST	List & create job applications
Models Overview

    CustomUser: Extends Django user with role field (admin/user)

    Category: Job categories (e.g. Engineering, Marketing)

    Job: Job postings with title, description, location, job_type, salary, company, category

    Application: Job applications with applicant name, email, resume upload, cover letter

Search Optimization

    pg_trgm extension is required on PostgreSQL for trigram similarity searches

    GIN indexes are created on title, description, company, and location fields to speed up searches

Deployment

    Configure environment variable DATABASE_URL with your PostgreSQL database URL

    Make sure pg_trgm is enabled on your database

    Use a WSGI server like Gunicorn for production deployment

