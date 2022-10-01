from tabnanny import verbose
from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(verbose_name="Full Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    Phone = models.IntegerField(verbose_name="Phone")
    
    