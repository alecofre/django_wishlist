from django.urls import path
from . import views 

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
     path('/create_wish', views.create_wish, name='create_wish'),
     path('/add2MyList/<item_id>', views.add2MyList, name='add2MyList'),
     path('/remove2MyList/<item_id>', views.remove2MyList, name='remove2MyList'),
     path('/delete/<item_id>', views.delete, name='delete'),
     # path('/wish_items/create', views.create_wish_form, name='create_wish_form'),
     # path('/register', views.register, name='register'),
     # path('/login', views.login, name='login'),
]