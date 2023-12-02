from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewsForm, PersonForm, UserRegisterForm, UserLoginForm
from .models import News, Category, Profession
from .models import Human


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


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/home_news_list.html'
    extra_context = {'title': "Главная"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related("category")


class NewsByCategory(ListView):
    model = News
    template_name = 'News/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    extra_context = {'title': "Категории"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related("category")


class ViewNews(DetailView):
    model = News
    context_object_name = "news_item"
    template_name = 'News/view_news.html'


class AddNews(CreateView):
    form_class = NewsForm
    template_name = "News/add_news.html"
    login_url = "/admin/"


class PeopleList(ListView):
    model = Human
    context_object_name = 'people'
    template_name = "People/peopleList.html"
    extra_context = {'title': "Список людей"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список людей"
        return context


class PeopleByProfession(ListView):
    model = Human
    context_object_name = 'people'
    template_name = "People/peopleList.html"
    allow_empty = False
    extra_context = {'title': "Профессии"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Profession.objects.get(pk=self.kwargs['profession_id']).title
        return context


class ViewPerson(DetailView):
    model = Human
    context_object_name = "person_item"
    template_name = "People/view_person.html"


class AddPerson(CreateView):
    form_class = PersonForm
    template_name = "People/add_person.html"
    login_url = "/admin/"
