from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('loginForm', views.loginForm),
    path('signupForm', views.signupForm),
    path('storeForm', views.storeForm)
]
