# Generated by Django 5.0.6 on 2024-07-08 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_user_favoritelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favoriteList',
            field=models.JSONField(default=str, verbose_name='json'),
        ),
    ]
