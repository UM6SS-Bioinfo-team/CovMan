from .serializers import *
from django.contrib.auth.models import User
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ..models import *

@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def patient_list(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = PatientSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
def patient_detail(request, pk):
   
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def virus_list(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = VirusSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VirusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
def virus_detail(request, pk):
   
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VirusSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VirusSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def ace_list(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = ACESerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ACESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
def ace_detail(request, pk):
   
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ACESerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ACESerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def virus_var_list(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = VirusVariantSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VirusVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
def virus_var_detail(request, pk):
   
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VirusVariantSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VirusVariantSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def ace_var_list(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = ACEVariantSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ACEVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
def ace_var_detail(request, pk):
   
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ACEVariantSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ACEVariantSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
