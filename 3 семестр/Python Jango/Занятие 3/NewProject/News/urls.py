from django.contrib import admin
from django.urls import path
from News.views import index, test, nothingSpecial

urlpatterns = [
    path('', index),
    path('test', test),
    path('nothingSpecial', nothingSpecial),
]
