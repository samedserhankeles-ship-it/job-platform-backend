ffrom django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    username = None 
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, default='user', choices=[('user','User'),('admin','Admin')])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    location_city = models.CharField(max_length=100, db_index=True) # İndeks eklendi
    created_at = models.DateTimeField(auto_now_add=True, db_index=True) # İndeks eklendi

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
