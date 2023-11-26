from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewsForm, PersonForm
from .models import News, Category, Profession
from .models import Human


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/home_news_list.html'
    extra_context = {'title': "Главная"}

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
