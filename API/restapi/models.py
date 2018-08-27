from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    
    class Meta:
        verbose_name_plural= 'Employee'