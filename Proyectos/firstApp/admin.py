from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'sal')


admin.site.register(Employee, EmployeeAdmin)
