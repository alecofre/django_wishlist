from django.urls import path
from . import views 

urlpatterns = [
     path('', views.login_page, name='login_page'),
     path('/register', views.register, name='register'),
     path('/login', views.login, name='login'),
     path('/logout', views.logout, name='logout'),
]