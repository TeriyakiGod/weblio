# Django Wagtail Template

A modern Django CMS template built with Wagtail, featuring Docker containerization and automated deployment.

## Features

- **Wagtail CMS** - Powerful content management system with rich page editing
- **PostgreSQL** - Production-ready database with full-text search
- **Docker** - Containerized development and deployment
- **Multi-environment setup** - Separate requirements for development and production
- **Pre-commit hooks** - Code quality enforcement with Black, flake8, isort, and mypy
- **GitHub Actions** - Automated CI/CD pipeline with CapRover deployment
- **Environment-based configuration** - Secure settings management with python-decouple
- **Debug toolbar** - Enhanced development debugging (dev environment only)
- **Testing framework** - pytest and pytest-django for robust testing
- **WhiteNoise** - Simplified static file serving for production

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd django-wagtail-template
   ```

2. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

3. **Run migrations and collect static files**
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --noinput
   ```

4. **Create a superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Local Development (without Docker)

1. **Start the database**
   ```bash
   docker-compose up db
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations and collect static files**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file with:
```env
DJANGO_SECRET_KEY=your-secret-key
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
WAGTAIL_SITE_NAME=Django Wagtail Template
```

## Deployment to CapRover

### 1. Deploy MinIO for Media Storage

First, create a MinIO instance for media file storage:

1. **Create a new CapRover app** called `minio-storage`
2. **Use Docker image**: `minio/minio:latest`
3. **Set environment variables**:
   ```env
   MINIO_ROOT_USER=admin
   MINIO_ROOT_PASSWORD=your-strong-password-here
   ```
4. **Set startup command**: `server /data --console-address ":9001"`
5. **Add persistent directory**:
   - Path in App: `/data`
   - Label: `minio-data`
6. **Enable HTTPS** and note your MinIO URL (e.g., `https://minio-storage.yourdomain.com`)

### 2. Create Django App

1. **Create a CapRover app**
   - Log in to your CapRover dashboard, create a new app, and name it (e.g., `django-wagtail-template`).

2. **Set environment variables**
   - Add the following in the app's "Environment Variables" section:
      ```env
      # Django Settings Module
      DJANGO_SETTINGS_MODULE=mysite.settings.production

      # Core Settings
      DJANGO_SECRET_KEY=your-secret-key
      DEBUG=False
      POSTGRES_DB=postgres
      POSTGRES_USER=postgres
      POSTGRES_PASSWORD=postgres
      POSTGRES_HOST=postgres
      POSTGRES_PORT=5432
      WAGTAIL_SITE_NAME=Django Wagtail Template

      # MinIO Configuration
      MINIO_ACCESS_KEY=admin
      MINIO_SECRET_KEY=your-strong-password-here
      MINIO_BUCKET_NAME=django-media
      MINIO_ENDPOINT_URL=https://minio-storage.yourdomain.com
      MINIO_USE_SSL=True
      MINIO_REGION_NAME=eu-east-1

      # Email Configuration
      EMAIL_HOST=smtp.gmail.com
      EMAIL_PORT=587
      EMAIL_USE_TLS=True
      EMAIL_HOST_USER=your-email@example.com
      EMAIL_HOST_PASSWORD=your-email-password

      # Security Settings
      ALLOWED_HOSTS=yourdomain.com,localhost,127.0.0.1
      CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://subdomain.yourdomain.com
      WAGTAILADMIN_BASE_URL=https://yourdomain.com

      LOG_LEVEL=info
      ```

### 3. Create MinIO Bucket

1. **Access MinIO Console**: Go to `https://minio-storage.yourdomain.com:9001`
2. **Login** with your MinIO credentials
3. **Create bucket** named `django-media` (or whatever you set in `MINIO_BUCKET_NAME`)
4. **Set bucket policy** to allow public read access if needed

### 4. Deploy via GitHub Actions

Configure `CAPROVER_SERVER`, `APP_NAME`, and `APP_TOKEN` as repository secrets. Push changes to trigger deployment.

## Tech Stack

### Core Framework
- **Django 5.2.3** - High-level Python web framework
- **Wagtail 7.0.1** - Django-based CMS with rich editing experience
- **PostgreSQL** - Advanced open-source relational database
- **Gunicorn** - Python WSGI HTTP server for production
- **Whitenoise** - Simplified static file serving for production

### Development Tools
- **django-debug-toolbar** - In-browser debugging and profiling
- **python-decouple** - Separation of configuration from code
- **pillow** - Python Imaging Library for image processing
- **pytest & pytest-django** - Testing framework with Django integration

### Code Quality
- **pre-commit** - Git hooks for code quality
- **Black** - Python code formatter
- **flake8** - Python linting tool
- **isort** - Import sorting utility
- **mypy** - Static type checking

### Infrastructure
- **Docker & Docker Compose** - Containerization and orchestration
- **GitHub Actions** - CI/CD automation
- **CapRover** - Platform-as-a-Service deployment
