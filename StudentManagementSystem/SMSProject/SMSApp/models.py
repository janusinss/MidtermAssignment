from django.db import models
from .models import models
# Create your models here.

class Students(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    DateOfBirth = models.CharField(max_length=100)
    Course = models.CharField(max_length=100)
    EnrollmentDate = models.DateField()