# Todoo - Task Management App

**Todoo** is a task management app that lets users create, update, and track tasks with status updates, descriptions, and photo uploads.

## Features
- Create, update, and delete tasks.
- Display all your to-do task.
- Track task status (Pending, In Progress, Completed).
- Upload and display photos for each task.
- User authentication and management.

## Tech Stack
- **Backend**: Django
- **Database**: PostgreSQL (NEON)
- **Cloud Storage**: Cloudinary (for media file storage)
- **Frontend**: Bootstrap 5
- **Authentication**: Django Authentication

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- Cloudinary account (for media file storage)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/todoo.git
cd todoo
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
```

### 3. Activate a virtual environment
```bash
# macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Create and configure environment variables
```bash
# create .env
cp sample.env .env
3 and set up your environment variables in .env
```
### 6. Apply migrations
```bash
# if there are no migrations before
python3 manage.py makemigrations
python3 manage.py migrate
```

## 7. Run the development server
```bash
python manage.py runserver
```
