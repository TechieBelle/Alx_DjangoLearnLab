from django.urls import path, include
from . import views
from.views import post_list, post, login, register  

urlpatterns = [
    path('',views.post_list, name = 'home'),  
    path('posts/', views.post, name='posts'),
    path('login/',views.login, name = 'login'),  
    path('register/',views.register, name = 'register'), 

]