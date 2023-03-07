from django.urls import path
from . import views

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('button',views.button,name='button'),
    path('form',views.form,name='form'),
    path('msg',views.msg,name='msg'),



]