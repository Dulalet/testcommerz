from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class ListEmployees(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['uuid', 'name', 'position', 'employment_date', 'salary', 'employee__name']


class CreateEmployee(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployee(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployee(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
