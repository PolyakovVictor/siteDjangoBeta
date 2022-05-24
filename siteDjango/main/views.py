from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")


def loginForm(request):
    return render(request, "main/loginForm.html")


def signupForm(request):
    return render(request, "main/signupForm.html")


def storeForm(request):
    return render(request, "main/storeForm.html")


def about(request):
    return HttpResponse("<h4>About</h4>")
