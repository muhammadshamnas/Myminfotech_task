from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status , generics
from . serializers import *
from . models import Store
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse, JsonResponse
'''
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
'''   
    
    
class StoreListView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    
    def get(self,request,format=None):
        Userse=Store.objects.all()
        serializer=StoreSerializer(Userse,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StoreDataCreation(APIView):
    
    serializer_class = StoreSerializer

    
    def post(self, request, *args, **kwargs):
        serializer= StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name=serializer.validated_data.get('username',None)
        address=serializer.validated_data.get('first_name',None)
        menu=serializer.validated_data.get('email',None)
        menu=serializer.validated_data.get('password',None)
        serializer.save()
        print(password)
        print(self.request.user)
        try:
            ce=Newmodel.objects.create(username=username,first_name=first_name,email=email,password=password,last_name=last_name)
            
            return Response(data={'detail': 'Store Details created successfully'}, status=status.HTTP_201_CREATED)

        except:
            return self.user
            return Response(data={'detail': 'Store Details creation Failed'}, status=status.HTTP_400_FAILED)
        
        
        
        
class RetrieveUpdateDestroyStoreAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class StoreList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Store.objects.all().order_by('id')
        serializer = StoreSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class TodoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Store().objects.get(pk=pk)
        except :
            return Response(data={'detail': 'Store Details creation Failed'})
    
 
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StoreSerializer(snippet)
        return Response(serializer.data)


    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

  
    
    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
 
  