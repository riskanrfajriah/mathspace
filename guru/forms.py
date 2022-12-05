from dataclasses import fields
from django.forms import ModelForm
from django import forms
from guru.models import dataguru

class FormGuru(ModelForm):
    class Meta:
        model = dataguru
        fields = '__all__'
        