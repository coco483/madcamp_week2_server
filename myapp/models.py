from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()