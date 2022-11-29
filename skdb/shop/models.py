from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Customer(models.Model):
    cstid = models.IntegerField()
    cstname = models.CharField(max_length = 70)
    cstemail = models.EmailField(max_length = 70)
    cstpass = models.CharField(max_length = 70)
    cstbill = models.IntegerField(max_length = 70)

    def __str__(self):
        return self.cstname