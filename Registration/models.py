from pyexpat import model
from django.db import models

# Create your models here.
class emp_details(models.Model):
    name = models.CharField(max_length=10) 
    emp_id = models.CharField(max_length=10) 
    email=models.EmailField()
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100) 
    phone_no = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='pics')
    password=models.CharField(max_length=20)

class announcements(models.Model):
    name = models.CharField(max_length=10) 
    info = models.TextField(max_length=1000) 