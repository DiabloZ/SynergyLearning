from django.urls import path

from News.views import HomeNews, NewsByCategory, ViewNews, AddNews
from News.views import human, get_profession, view_person, add_person

urlpatterns = [
    path('', HomeNews.as_view(), name='Home'),
    path('people', human, name='People'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>', ViewNews.as_view(), name='View_news'),
    path('profession/<int:profession_id>', get_profession, name='Profession'),
    path('person/<int:person_id>', view_person, name='View_person'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('person/add_person', add_person, name='Add_person')
]
