from django import forms
from django.db import models
from django.urls import reverse, reverse_lazy
from datetime import *

# Create your models here.

class Edit_Overdue_Charges(models.Model):
    overdue = models.CharField(max_length=5)

    def __str__(self):
        return 'The current overdue charges is ' + self.overdue + ' naira per day (click to edit)'

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
        ordering = ['registration_date']
        verbose_name_plural = 'students'

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15, unique=True)
    Email = models.EmailField()
    phone_number = models.CharField(max_length=11, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    year_of_admission = models.ForeignKey(Year_Of_Reg, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    level = models.CharField(
        max_length=5,
        choices=CHOICES,
    )


    def get_absolute_url(self):
        return reverse('scanner:profile', kwargs={'student_id': self.pk })

    def save(self):
        # self.calcReturnDate()
        super().save()  # Call the "real" save() method.

    def __str__(self):
        return self.first_name.title() + ' ' + self.second_name.title()


class Book(models.Model):
    class Meta:
        ordering = ['-issued_date']

    title = models.CharField(max_length=100)
    ret_date = models.CharField(max_length=200, null=True, blank=True)
    borrowed_by = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    issued_date = models.DateTimeField(auto_now_add=True)
    added_days = models.IntegerField(blank=True, null=True)
    rem_days = models.CharField(max_length=100, null=True, blank=True)

    def calcReturnDate(self):
        # date and time functions to calculate returning date
        current_date = date.today()
        t1 = timedelta(days=14)
        dateOfReturn = current_date + t1
        self.returning_date = dateOfReturn
        return dateOfReturn

    def get_absolute_url(self):
        return reverse('scanner:profile', kwargs={'student_id': self.borrowed_by.pk })

    def __str__(self):
        return self.title[:50]


