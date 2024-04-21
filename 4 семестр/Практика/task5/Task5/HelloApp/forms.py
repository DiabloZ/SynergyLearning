import re
import string

from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Person


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


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя",
        help_text="150 символов максимум",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    ),
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя",
        help_text="150 символов максимум",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')

