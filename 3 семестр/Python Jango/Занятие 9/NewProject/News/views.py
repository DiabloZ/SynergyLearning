from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category, Profession
from .models import Human


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': "Список новостей",
        'categories': categories
    }
    return render(request, 'News/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, 'News/category.html', context=context)


def human(request):
    people = Human.objects.all()
    professions = Profession.objects.all()
    context = {
        'people': people,
        'title': "Список людей",
        'professions': professions
    }
    return render(request, 'People/peopleList.html', context)


def get_profession(request, profession_id):
    people = Human.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'people': people,
        'professions': professions,
        'profession': profession
    }
    return render(request, 'People/profession.html', context=context)


def test(request):
    return HttpResponse('<h3>Test пейдж</h3>')


def nothingSpecial(request):
    return HttpResponse('<h2>Страничка с одной строчкой, ничего особенного.</h2>')
