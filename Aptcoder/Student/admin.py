from django.contrib import admin
from Student.models import Student, StudentCourse

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentCourse)