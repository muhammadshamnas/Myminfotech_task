from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Store(models.Model):

    name=models.CharField(max_length=100,unique=True,null=False)
    address=models.CharField(max_length=400,null=False)
    menu=models.CharField(max_length=200,null=False)
    price=models.IntegerField(null=False)
    
    

    

    class Meta:
        verbose_name_plural = "Store"

    def __str__(self):
        return self.name

    


