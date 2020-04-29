from django.db import models
from datetime import datetime


# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return self.rollNo + "\t" + self.firstName + "\t" + self.lastName


class AuditTrail(models.Model):
    rollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    comments = models.CharField(max_length=100)
    dateAdded = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.rollNo + "\t" + self.comments + "\t" + self.dateAdded