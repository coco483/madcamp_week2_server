# Generated by Django 5.0.6 on 2024-07-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('displayName', models.CharField(max_length=100)),
            ],
        ),
    ]
