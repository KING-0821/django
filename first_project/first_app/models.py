from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    deadline = models.DateField()

    def __str__(self) -> str:
        return self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username