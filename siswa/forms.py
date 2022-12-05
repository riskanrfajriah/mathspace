from dataclasses import fields
from django.forms import ModelForm
from django import forms
from siswa.models import datasiswa

class FormSiswa(ModelForm):
    class Meta:
        model = datasiswa
        fields = '__all__'
        