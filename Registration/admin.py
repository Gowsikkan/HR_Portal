from django.contrib import admin
from .models import announcements, emp_details,Attendance
# Register your models here.

admin.site.register(emp_details)
admin.site.register(announcements)
admin.site.register(Attendance)
