from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import Userdataserializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status , generics
from . models import Userdata
from . import models
# Create your views here.




class Userdata(APIView):
    '''
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    '''
    serializer_class = Userdataserializer
    queryset = Userdata.objects.all()
    
    
    

    def post(self, request, *args, **kwargs):
        
        serializer = Userdataserializer(data=request.data)

        serializer.is_valid(raise_exception=True)
      
        name =serializer.validated_data.get('name',None)
        email=serializer.validated_data.get('email',None)
        phonenumber: str=serializer.validated_data.get('phonenumber',None)
        place:str=serializer.validated_data.get('place',None)
        country:str=serializer.validated_data.get('country',None)
        password :str =serializer.validated_data.get('password',None)
        print(serializer.data)
        try:
    
            models.Userdata.objects.create(name=name, email= email,phonenumber=phonenumber, place=place, country=country,password=password)
            return Response(data={'detail':'Sucess'},status=status.HTTP_201_CREATED)
        except :
            return Response(data={"detail": "faild"}, status=status.HTTP_400_BAD_REQUEST)
   