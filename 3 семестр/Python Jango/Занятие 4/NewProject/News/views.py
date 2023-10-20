from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('<h1>Hello World</h1>')


def test(request):
    return HttpResponse('<h3>Test пейдж</h3>')


def nothingSpecial(request):
    return HttpResponse('<h2>Страничка с одной строчкой, ничего особенного.</h2>')
