from django.db import models

# Create your models here.
class List(models.Model):
    task_number = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=20)
    task_status = models.CharField(max_length=20)
