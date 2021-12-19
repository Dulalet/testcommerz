from django.urls import path

from employees.views import *

urlpatterns = [
    path('employees/', ListEmployees.as_view(), name="employees"),
    path('employees/create/', CreateEmployee.as_view(), name="employee-create"),
    path('employees/<uuid:pk>/', UpdateEmployee.as_view(), name="employee-update"),
    path('employees/<uuid:pk>/delete/', DeleteEmployee.as_view(), name="employee-delete"),
]
