from django.contrib import admin
from django.urls import path
from News.views import index, test, nothingSpecial, human

urlpatterns = [
    path('', index),
    path('people', human),
    path('test', test),
    path('nothingSpecial', nothingSpecial),
]
