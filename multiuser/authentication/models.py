from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    address=models.TextField(default="")

    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    def __str__(self):
        return self.username

# Create your models here.
