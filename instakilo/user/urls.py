"""urls file for user
    """

from django.urls import path

from user.views import Login
from user.views import Registeration


urlpatterns = [path("login/", Login.as_view(), name="Login")]
urlpatterns = [path("register/", Registeration.as_view(), name="Registeration")]
