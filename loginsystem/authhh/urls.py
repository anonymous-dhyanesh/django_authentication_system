from django.urls import path
from . import views

app_name = 'authhh'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name='logoutUser')
]
