from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.users_login, name="login"),
    path("logout/", views.users_logout, name="logout"),
    path("signup/", views.users_signup, name="signup"),
    path("login/kakao/", views.kakao_login, name="kakao_login"),
    path(
        "login/kakao/callback/",
        views.kakao_login_callback,
        name="kakao_callback",
    ),
]