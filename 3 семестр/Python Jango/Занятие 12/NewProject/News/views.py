from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

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
        return News.objects.filter(is_published=True)


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
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = "news_item"
    template_name = 'News/view_news.html'


class AddNews(CreateView):
    form_class = NewsForm
    template_name = "News/add_news.html"


def view_person(request, person_id):
    person_item = get_object_or_404(Human, pk=person_id)
    context = {
        'person_item': person_item
    }
    return render(request, 'People/view_person.html', context=context)


def human(request):
    people = Human.objects.all()
    context = {
        'people': people,
        'title': "Список людей"
    }
    return render(request, 'People/peopleList.html', context)


def get_profession(request, profession_id):
    people = Human.objects.filter(profession_id=profession_id)
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'people': people,
        'profession': profession
    }
    return render(request, 'People/profession.html', context=context)


def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = PersonForm()
    return render(request, 'People/add_person.html', context={"form": form})
