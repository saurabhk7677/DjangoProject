from django.contrib import admin
from django.urls import path
from . models import Employee
# Register your models here.

#@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid', 'ename', 'eemail', 'econtact')

admin.site.register(Employee)


