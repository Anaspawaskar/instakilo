"""admin class for user
    """
from django.contrib import admin
from user.models import UserModel


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """imported user"""


admin.site.register(UserModel, UserAdmin)
