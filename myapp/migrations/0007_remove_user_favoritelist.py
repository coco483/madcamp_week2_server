# Generated by Django 5.0.6 on 2024-07-07 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_stock_alter_user_id_user_favoritelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favoriteList',
        ),
    ]
