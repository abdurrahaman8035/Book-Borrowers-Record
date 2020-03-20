from django import forms
from django.db import models
from django.urls import reverse
from datetime import *
# Create your models here.

class Year_Of_Reg(models.Model):
    year = models.CharField(max_length=9)

    def __str__(self):
        return self.year.title()


CHOICES = [
        ('100', '100 L'),
        ('200', '200 L'),
        ('300', '300 L'),
        ('400', '400 L'),
        ('500', '500 L'),
    ]


class Student(models.Model):
    class Meta:
        ordering = ['-registered_date']
    
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    Email = models.EmailField()
    registered_date = models.DateTimeField(auto_now_add=True)
    year_of_admission = models.ForeignKey(Year_Of_Reg, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    level = models.CharField(
        max_length=5,
        choices=CHOICES,
    )

    def get_absolute_url(self): # new
        return reverse('students_list')
    def __str__(self):
        return self.first_name.title() + ' ' + self.second_name.title()

class Book(models.Model):
    class Meta:
        ordering = ['-issued_date']

    title = models.CharField(max_length=100)
    borrowed_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(auto_now_add=True)
    returning_date = models.DateTimeField()

    def calcReturnDate(self):
        # date and time functions to calculate returning date
        current_date = date.today()
        t1 = timedelta(days=14)
        dateOfReturn = current_date + t1
        self.returning_date = dateOfReturn
        return dateOfReturn

    #calculate the date before saving the form data
    def save(self):
        self.calcReturnDate()
        super().save()  # Call the "real" save() method.

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self): # new
        return reverse('BookList')