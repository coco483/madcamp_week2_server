# Generated by Django 5.0.6 on 2024-07-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_user_favoritelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favoriteList',
            field=models.JSONField(default=list, verbose_name='json'),
        ),
    ]
