from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Person

from .forms import PersonForm


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

