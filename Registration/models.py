from django.db import models
from django.utils import timezone
from datetime import date

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

class Attendance(models.Model):
    user = models.BigIntegerField(null=True)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    hours_worked=models.BigIntegerField(null=True)
    date=models.DateField(null=True)
    present=models.BooleanField(default=False)
    def check_date(self):
        self.date=date.today()
        self.save()
    def check_out_user(self):
        self.check_out = timezone.now()
        
        check_in_time = self.check_in
        check_out_time = self.check_out
        hours_worked = (check_out_time - check_in_time).total_seconds() / 3600
        self.hours_worked = hours_worked
        if hours_worked>=8:
            self.present = True
        self.save()

