import string

from django import forms

from django.db import models
from .models import Person
import re
from django.core.exceptions import ValidationError


class PersonForm(forms.ModelForm):

    def clean(self):
        name: string = self.cleaned_data['name']
        people = Person.objects.filter(name=name).first()

        if name == "":
            raise ValidationError('Нужно ввести хотябы одну букву')
        if re.match(r'\d', name):
            raise ValidationError('Имя должно начинаться с буквы')
        if people is not None:
            if people.name == name:
                raise ValidationError('Вас уже приветствуют на главной страничке')

        return self.cleaned_data

    class Meta:
        model = Person
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={"class": "form-control"}
            )
        }
