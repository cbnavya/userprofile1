from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions
from rest_framework import serializers

from user.serializer import UserSerializer,UserProfileSerializer
# Create your views here.


class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class UserProfileView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def update(self,request,*args,**kwargs):
        id=int(kwargs.get("pk"))
        user_obj=request.user.profile
        if request.user.profile.id == id:
            serializer=UserProfileSerializer(data=request.data,instance=user_obj)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            raise serializers.ValidationError("permission denied")      