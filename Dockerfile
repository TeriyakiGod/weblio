FROM python:3.12-slim-bookworm

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    LOG_LEVEL=info

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install the project requirements.
COPY requirements/ /requirements/
RUN pip install -r /requirements/production.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Copy the source code of the project into the container.
COPY . .

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

CMD set -xe; gunicorn mysite.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --threads 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level $LOG_LEVEL
