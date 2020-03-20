from django.contrib import admin
from .models import Student, Year_Of_Reg, Book

# Register your models here.
admin.site.register(Student)
admin.site.register(Year_Of_Reg)
admin.site.register(Book)
