from django.urls import path

from News.views import index, human, get_category, get_profession, view_news, view_person, add_news

urlpatterns = [
    path('', index, name='Home'),
    path('people', human, name='People'),
    path('category/<int:category_id>', get_category, name='Category'),
    path('news/<int:news_id>', view_news, name='View_news'),
    path('profession/<int:profession_id>', get_profession, name='Profession'),
    path('person/<int:person_id>', view_person, name='View_person'),
    path('news/add_news', add_news, name='Add_news')
]
