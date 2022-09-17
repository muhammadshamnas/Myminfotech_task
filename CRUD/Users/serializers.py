from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Userdata

class Userdataserializer(serializers.ModelSerializer):

    
    name = serializers.CharField( max_length=30, required=True)
    email= serializers.CharField(max_length=100)
    phonenumber = serializers.CharField(max_length=120)
    place = serializers.CharField(max_length=80, required=True)
    country = serializers.CharField(max_length=30, required=True)
    password=serializers.CharField(max_length=30)
    
    class Meta:
        model=Userdata
        fields='__all__'