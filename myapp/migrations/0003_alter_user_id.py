# Generated by Django 5.0.6 on 2024-07-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]