# Generated by Django 2.1.5 on 2020-06-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]