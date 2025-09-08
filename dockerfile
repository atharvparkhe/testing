# FROM python:3.11-slim

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#         build-essential \
#         libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# RUN mkdir -p /app/static /app/data

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]


# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for psycopg2 & pillow if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose app port
EXPOSE 8000

# Run migrations + start server
CMD ["gunicorn", "project_root.wsgi:application", "--bind", "0.0.0.0:8000"]
