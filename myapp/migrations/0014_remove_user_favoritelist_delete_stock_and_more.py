# Generated by Django 5.0.6 on 2024-07-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_stock_market'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favoriteList',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='user',
            name='favoriteList',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
