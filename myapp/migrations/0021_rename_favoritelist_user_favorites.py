# Generated by Django 5.0.6 on 2024-07-08 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_user_favoritelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='favoriteList',
            new_name='favorites',
        ),
    ]
