from django.contrib import messages
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Person

from .forms import PersonForm, UserRegisterForm, UserLoginForm


class PersonHello(ListView):
    model = Person
    context_object_name = 'hello'
    template_name = 'HelloScreen/hello_screen.html'
    extra_context = {'title': "Страница приветствия"}


class AddPerson(CreateView):
    form_class = PersonForm
    template_name = "AddPerson/add_person.html"
    success_url = reverse_lazy('Home')
    login_url = "/admin/"


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно")
            user = form.save()
            login(request, user)
        else:
            messages.error(request, "Не успешно")
    else:
        form = UserRegisterForm()
    return render(request, 'Auth/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("Home")
    else:
        form = UserLoginForm()
    return render(request, 'Auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Login')
