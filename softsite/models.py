from django.db import models
from datetime import datetime


# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)


class AuditTrail(models.Model):
    id = models.AutoField(primary_key=True)
    rollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    comments = models.CharField(max_length=100)
    # dateAdded = models.DateTimeField(default=datetime.now(), blank=True)