"""model class for user
    """
from django.db import models
from django.contrib.auth.models import User

# Create your models here


class UserModel(User):
    """created a class for user

    Args:
        User (_type_): _description_
    """

    is_email_verified = models.BooleanField(default=False)
