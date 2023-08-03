from django.urls import path
from .views import *


urlpatterns = [
   
    path("",index,name='index'),
    path("register/",register,name ='register'),
    path("login/", login_view, name ='Login'),
    path("logut/", logout_view, name ='Logout'),
    path("edit_note", edit_note, name ='EditNote'),
]
