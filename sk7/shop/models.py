from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Shopshirt(models.Model):
    custid=models.IntegerField()
    custname=models.CharField(max_length=70)
    custemail=models.EmailField(max_length=70)
    custpass=models.CharField(max_length=70)
    custbill=models.IntegerField(max_length=70)

    def __str__(self):
        return self.custname










