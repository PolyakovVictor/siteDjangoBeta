from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('loginForm', views.loginForm),
    path('signupForm', RegisterUser.as_view(), name='signupform'),
    path('storeForm', views.storeForm),
]
