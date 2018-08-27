from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EmployeeList, name ='list_employees')
]