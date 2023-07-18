from django. urls import path
from . import views

app_name = "insuranceapp"
urlpatterns = [
    path("reg/", views.user_reg, name="user_reg"),
    path("login/", views.user_login, name="user_login"),

    ]