from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=12)
    age=models.IntegerField()
    rollno=models.IntegerField()

    def __str__(self):
        return str(self.name)