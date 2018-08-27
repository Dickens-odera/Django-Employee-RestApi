from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializers(employees, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        pass