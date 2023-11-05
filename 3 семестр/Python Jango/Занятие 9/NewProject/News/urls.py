from django.urls import path

from News.views import index, test, nothingSpecial, human, get_category, get_profession

urlpatterns = [
    path('', index, name='Home'),
    path('people', human, name='People'),
    path('test', test),
    path('nothingSpecial', nothingSpecial),
    path('category/<int:category_id>', get_category, name='Category'),
    path('profession/<int:profession_id>', get_profession, name='Profession')
]
