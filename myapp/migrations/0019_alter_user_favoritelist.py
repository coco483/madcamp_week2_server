# Generated by Django 5.0.6 on 2024-07-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_user_favoritelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favoriteList',
            field=models.CharField(max_length=100),
        ),
    ]