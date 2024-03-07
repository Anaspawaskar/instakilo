"""urls file for user
    """

from django.urls import path

from user.views import Login
from user.views import Registeration


urlpatterns = [
    path("login/", Login.as_view(), name="Login"),
    path("register/", Registeration.as_view(), name="Registeration"),
]
