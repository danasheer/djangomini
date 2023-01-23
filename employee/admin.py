from django.contrib import admin
from employee.models import Employee
# Register your models here.

# @admin.register(Employee)
# class EmploeeAdmin(admin.ModelAdmin):
#     list_display =["id","name","civilid",'phone_num']
#     list_display_links =["name","id"]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','civilid']
    list_display_links = ['id', 'name']