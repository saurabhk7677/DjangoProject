from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    company = models.CharField(max_length=70)
    salary = models.IntegerField()
    bank = models.CharField(max_length=70)
   
    