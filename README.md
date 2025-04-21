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

## Database
- **To-do item model**
```py
class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    photo = CloudinaryField(
        'todoo_photo',
        folder='todoo_app/photos/',
        blank=True,
        null=True,
        help_text="Upload an optional photo for this task"
    )
```
- **User model**: use default authenticated user model from Django

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
# and set up your environment variables in .env
```
### 6. Apply migrations
```bash
# if there are no migrations before
python3 manage.py makemigrations
python3 manage.py migrate
```

### 7. Run the development server
```bash
python manage.py runserver
```
## Code Explanation

### Model-View-Template (MVT) in Django

| Component | Description |
|----------|-------------|
| **Model** | Defines the structure of the database using Django ORM. Example: `Todo` model stores task title and status. |
| **View** | Handles logic between model and template. Example: `TodoListView` retrieves to-do data and passes it to the template. |
| **Template** | Renders UI using HTML Templates. Example: `todo_list.html` displays tasks in a list format with Bootstrap. |


### Layered Architecture
- Presentation layer: HTML Templates and URL Dispatcher, rendering UI and dispatch route through user browser.
- Business logic layer: Django Forms & Views, handling user request and form submission.
- Data access layer: Django ORM & Models, define database structure and query data from NEON through Django ORM.
- Database layer: NEON table.
