from django import forms
from .models import News, Human
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={"class": "form-control"}
            ),
            'content ': forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10
                }
            ),
            'category': forms.Select(
                attrs={"class": "form-control"}
            )
        }


class PersonForm(forms.ModelForm):

    def clean_firstName(self):
        firstName = self.cleaned_data['firstName']
        if re.match(r'\d', firstName):
            raise ValidationError('Имя не должно начинаться с цифр')
        return firstName

    def clean_surnameName(self):
        surnameName = self.cleaned_data['surnameName']
        if re.match(r'\d', surnameName):
            raise ValidationError('Фамилия не должна начинаться с цифр')
        return surnameName

    def clean_middleName(self):
        middleName = self.cleaned_data['middleName']
        if re.match(r'\d', middleName):
            raise ValidationError('Отчество не должно начинаться с цифр')
        return middleName

    class Meta:
        model = Human
        fields = ['firstName', 'surnameName', 'middleName', 'old', 'birthDay', 'profession']
        widgets = {
            'firstName': forms.TextInput(
                attrs={"class": "form-control"}
            ),
            'surnameName': forms.TextInput(
                attrs={"class": "form-control"}
            ),
            'middleName': forms.TextInput(
                attrs={"class": "form-control"}
            ),
            'old': forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            'birthDay': forms.DateInput(
                attrs={"class": "form-control"}
            ),
            'profession': forms.Select(
                attrs={"class": "form-control"}
            )
        }

