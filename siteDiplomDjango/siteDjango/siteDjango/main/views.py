from audioop import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DataMixin


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


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/signupForm.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Signup")
        return dict(list(context.items()) + list(c_def.items()))
