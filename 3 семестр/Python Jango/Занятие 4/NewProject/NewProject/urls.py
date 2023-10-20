from django.contrib import admin
from django.urls import path,  include
from News.views import index
from News.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('News.urls')),
]
