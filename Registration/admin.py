from django.contrib import admin
from .models import announcements, emp_details
# Register your models here.

admin.site.register(emp_details)
admin.site.register(announcements)
