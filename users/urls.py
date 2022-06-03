from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("users", views.LoginView.as_view(), name="users"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete_verification")
]
