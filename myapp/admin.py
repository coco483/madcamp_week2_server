from django.contrib import admin
from .models import TodoItem
from .models import User

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(User)
