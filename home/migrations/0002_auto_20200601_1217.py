# Generated by Django 2.1.5 on 2020-06-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_date',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='task_time',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
