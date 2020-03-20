from django import forms
from django.db import models

choices = [
    ('100','100 level'),
    ('200','200 level'),
    ('300','300 level'),
    ('400','400 level'),
]
class RegForm(forms.Form):
    first_name = forms.CharField()
    second_name = forms.CharField()
    Email = forms.EmailField()
    registered_date = forms.DateField()
    year_of_admission = forms.ChoiceField(choices = choices)
    image_url = forms.URLField(max_length=100)

    