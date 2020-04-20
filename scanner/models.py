from django.db import models
from django.urls import reverse
from datetime import *


class Year_Of_Reg(models.Model):
    year = models.CharField(max_length=9)

    class Meta:
        verbose_name_plural = 'years of admission'

    def __str__(self):
        return self.year.title()


CHOICES = [
    ('100', '100 L'),
    ('200', '200 L'),
    ('300', '300 L'),
    ('400', '400 L'),
]


class Student(models.Model):
    """Database table for storing information
    about a particular student that borrowed a book"""
    class Meta:
        ordering = ['-registration_date']
        verbose_name_plural = 'students'

    image = models.ImageField(
        upload_to='images/', null=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15, unique=True)
    Email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    year_of_admission = models.ForeignKey(
        Year_Of_Reg, on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(
        max_length=5,
        choices=CHOICES,
    )

    def get_absolute_url(self):
        return reverse('scanner:profile', kwargs={'student_id': self.pk})

    def __str__(self):
        return self.first_name.title() + ' ' + self.second_name.title()


class Staff(models.Model):
    """Database table for storing information
    about a particular staff that borrowed a book"""
    class Meta:
        ordering = ['-registration_date']
        verbose_name_plural = 'staffs'
    image = models.ImageField(
        upload_to='images/', default='images/user-circle.svg')
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
    class Meta:
        ordering = ['-issued_date']

    title = models.CharField("Book title", max_length=100)
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
