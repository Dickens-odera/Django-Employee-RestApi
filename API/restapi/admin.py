from django.contrib import admin
from .models import Employee
# Register your models here.
 
class EmployeeModel(admin.ModelAdmin):
     model = Employee

admin.site.register(Employee, EmployeeModel)