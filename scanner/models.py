from django import forms
from django.db import models
from django.urls import reverse, reverse_lazy
from datetime import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

<<<<<<< HEAD
=======
class Edit_Overdue_Charges(models.Model):
    overdue = models.CharField(max_length=5)

    def __str__(self):
        return 'The current overdue charges is ' + self.overdue + ' naira per day (click to edit)'

>>>>>>> parent of 4e5a06c... Added styles to templates
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
        ordering = ['-registration_date']
        verbose_name_plural = 'students'

<<<<<<< HEAD
    image = models.ImageField(
        upload_to='images/', null=True)
=======
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/user-circle.svg')
>>>>>>> parent of 4e5a06c... Added styles to templates
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15, unique=True)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    year_of_admission = models.ForeignKey(Year_Of_Reg, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100, null=True, blank=True)
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


class Staff(models.Model):
    class Meta:
        ordering = ['-registration_date']
        verbose_name_plural = 'staffs'

    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/user-circle.svg')
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=15, unique=True)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('scanner:staffprofile', kwargs={'staff_id': self.pk})

    def __str__(self):
        return self.first_name.title() + ' ' + self.second_name.title()


class Book(models.Model):
<<<<<<< HEAD
    """create a book borrowed by a particular student"""
    class Meta:
        ordering = ['-issued_date']

    title = models.CharField("Book title", max_length=100)
    borrowed_by = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='books',
        null=True, blank=True)
    issued_date = models.DateTimeField(default=datetime.now())
    # added_days = models.IntegerField(null=True, blank=True)
    rem_days = models.CharField(max_length=100, null=True, blank=True)
    expiring_date = models.DateTimeField(
        default=(datetime.today() + timedelta(days=14)), null=True, blank=True)

    def get_absolute_url(self):
        student_id = self.borrowed_by.pk
        return reverse('scanner:profile', kwargs={'student_id': student_id})

    def __str__(self):
        return self.title[:50]


class Staff_Book(models.Model):
    """create a book borrowed by a particular staff"""
=======
>>>>>>> parent of 4e5a06c... Added styles to templates
    class Meta:
        ordering = ['-issued_date']

    title = models.CharField("Book title", max_length=100)
<<<<<<< HEAD
    borrowed_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name='books',
        null=True, blank=True)
    issued_date = models.DateTimeField(default=datetime.now())
    # added_days = models.IntegerField(null=True, blank=True)
    rem_days = models.CharField(max_length=100, null=True, blank=True)
    expiring_date = models.DateTimeField(
        default=(datetime.today() + timedelta(days=21)), null=True, blank=True)

    def get_absolute_url(self):
        staff_id = self.borrowed_by.pk
        return reverse('scanner:staffprofile', kwargs={'staff_id': staff_id})

    def __str__(self):
        return self.title[:50]

# class Edit_Overdue_Charges(models.Model):
#     overdue = models.IntegerField()

#     class Meta:
#         verbose_name_plural = 'overdue charges'

#     def __str__(self):
#         value = self.overdue
#         return 'The current overdue charges is ', value, ' naira per day'
=======
    borrowed_by = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    issued_date = models.DateTimeField(auto_now_add=True)
    # added_days = models.IntegerField(null=True, blank=True)
    rem_days = models.CharField(max_length=100, null=True, blank=True)
    expiring_date = models.DateTimeField(default=(datetime.today() + timedelta(days=14)), null=True, blank=True)

    def get_absolute_url(self):
        return reverse('scanner:profile', kwargs={'student_id': self.borrowed_by.pk })

    def __str__(self):
        return self.title[:50]
>>>>>>> parent of 4e5a06c... Added styles to templates
