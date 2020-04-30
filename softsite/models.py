from django.db import models
from datetime import datetime


# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)


class AuditTrail(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    rollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    comments = models.CharField(max_length=100)
    dateAdded = models.DateField(default=datetime.now(), blank=True)