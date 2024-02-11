"""app class for user
    """
from django.apps import AppConfig


class UserConfig(AppConfig):
    """userconfig class

    Args:
        AppConfig (_type_): _description_
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
