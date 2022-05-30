from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("users", views.LoginView.as_view(), name="users")
]
