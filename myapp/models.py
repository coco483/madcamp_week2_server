from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=5000)
    email = models.EmailField()
    displayName = models.CharField(max_length=100)
    favorites = models.JSONField('json', default=str)

    def __str__(self):
        return self.id