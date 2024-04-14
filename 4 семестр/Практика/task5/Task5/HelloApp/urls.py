from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page

from .views import PersonHello, AddPerson

urlpatterns = [
    path('', PersonHello.as_view(), name='Home'),
    path('add_person', AddPerson.as_view(), name='Add_person'),
]