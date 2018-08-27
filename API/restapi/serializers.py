from .models import Employee
from rest_framework import serializers
# Create your views here.
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','first_name','last_name','email']
        #fields = '__all__'
