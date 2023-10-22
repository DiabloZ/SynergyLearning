from django.shortcuts import render
from django.http import HttpResponse

from .models import News
from .models import Human


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей"
    }
    return render(request, 'index.html', context)


def human(request):
    people = Human.objects.all()
    context = {
        'people': people,
        'title': "Список людей"
    }
    return render(request, 'peopleList.html', context)


def test(request):
    return HttpResponse('<h3>Test пейдж</h3>')



def nothingSpecial(request):
    return HttpResponse('<h2>Страничка с одной строчкой, ничего особенного.</h2>')
