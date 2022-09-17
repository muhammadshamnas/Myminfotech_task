from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from . models import Store


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
    
    
class StoreSerializer(serializers.ModelSerializer):

    
    name = serializers.CharField( max_length=30, required=True)
    address=serializers.CharField(max_length=400)
    menu = serializers.CharField(max_length=120)
    price = serializers.CharField(max_length=80, required=True)
   
        
    class Meta:
        model=Store
        fields=('id','name', 'address', 'menu', 'price')
      
        