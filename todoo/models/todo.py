import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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