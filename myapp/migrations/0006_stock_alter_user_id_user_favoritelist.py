# Generated by Django 5.0.6 on 2024-07-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=5000, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='favoriteList',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='myapp.stock'),
        ),
    ]