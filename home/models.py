from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    test_title = models.CharField(max_length=10)
    test_desc = models.TextField()
    task_date = models.CharField(max_length=12)
    task_time = models.CharField(max_length=12)
    raw_date_time = models.CharField(max_length=20)
    # created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task_id} - {self.test_title}"