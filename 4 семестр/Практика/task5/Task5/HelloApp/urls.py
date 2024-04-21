from django.urls import path

from .views import PersonHello, AddPerson, register, user_login, user_logout

urlpatterns = [
    path('', PersonHello.as_view(), name='Home'),
    path('add_person', AddPerson.as_view(), name='Add_person'),
    path('register', register, name='Register'),
    path('login', user_login, name='Login'),
    path('logout', user_logout, name='Logout'),
]