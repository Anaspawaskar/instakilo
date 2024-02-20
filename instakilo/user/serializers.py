"""creating the serializer for user
    """
from rest_framework import serializers


class Loginserializer(serializers.Serializer):
    """form for the login page

    Args:
        serializers (_type_): _description_
    """

    username = serializers.CharField()
    password = serializers.CharField()


class Regsitrationclass(serializers.Serializer):
    """class for registration

    Args:
        serializers (_type_): _description_
    """

    mobile_number = serializers.IntegerField()
    email_id = serializers.EmailField()
    full_name = serializers.CharField()
    user_name = serializers.CharField()
    password = serializers.CharField()
