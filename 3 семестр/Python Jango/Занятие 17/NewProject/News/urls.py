from django.urls import path

from News.views import HomeNews, NewsByCategory, ViewNews, AddNews, register, user_login, user_logout
from News.views import PeopleList, PeopleByProfession, ViewPerson, AddPerson

urlpatterns = [
    path('', HomeNews.as_view(), name='Home'),
    path('news/<int:pk>', ViewNews.as_view(), name='View_news'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('register', register, name='Register'),
    path('login', user_login, name='Login'),
    path('logout', user_logout, name='Logout'),

    path('people', PeopleList.as_view(), name='People'),
    path('person/<int:pk>', ViewPerson.as_view(), name='View_person'),
    path('profession/<int:profession_id>', PeopleByProfession.as_view(), name='Profession'),
    path('person/add_person', AddPerson.as_view(), name='Add_person')
]
