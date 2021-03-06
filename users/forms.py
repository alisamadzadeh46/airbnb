from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpView(UserCreationForm):
    # use UserCreationForm
    # class Meta:
    #     model = models.User
    #     fields = ("first_name", "last_name", "email")
    #
    # password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    username = forms.EmailField(label="Email")
