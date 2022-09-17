from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Userdata(models.Model):
    name = models.CharField( max_length=30, null=True)
    email= models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=120)
    place = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    password=models.CharField(max_length=30)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Userdata"

