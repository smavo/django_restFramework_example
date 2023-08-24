from django.contrib import admin
from cbvApp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')


admin.site.register(Student, StudentAdmin)
