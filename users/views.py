from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        data = {
            "form": form,
        }
        return render(request, "users/login.html", data)

    def post(self, request):
        form = forms.LoginForm(request.POST)

