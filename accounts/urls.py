from django.urls import path
from .views import auth_view,logout_view

app_name = "accounts"

urlpatterns = [
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),

]
