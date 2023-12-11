
from django.urls import path
from .views import login_view, profile_viev, register, logout_viev


urlpatterns = [
    path("login/", login_view, name = "login"),
    path("profile/", profile_viev, name = "profile"),
    path("register/", register, name = "register"),
    path("exit/", logout_viev, name = "logout")
]
