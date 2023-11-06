from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category, Profession
from .models import Human


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей",
    }
    return render(request, 'News/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'News/category.html', context=context)


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
