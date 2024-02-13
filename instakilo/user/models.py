"""model class for user
    """
from django.db import models
from django.contrib.auth.backends import BaseBackend

# Create your models here


class UserModel(BaseBackend):
    """created a class for user

    Args:
        User (_type_): _description_
    """

    is_email_verified = models.BooleanField(default=False)
