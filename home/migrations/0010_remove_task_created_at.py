# Generated by Django 2.1.5 on 2020-06-03 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_task_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
    ]