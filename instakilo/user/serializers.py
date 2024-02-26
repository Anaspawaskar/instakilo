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
    user_name = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8, max_length=20)

    def validate_user_name(self, value):
        """validation for username"""

        if value == "":
            raise serializers.ValidationError("user_name cannot be empty")
        if not any(character.isdigit() for character in value):
            raise serializers.ValidationError("usename must contain a number")
        if len(value) < 8:
            raise serializers.ValidationError("password must contain 8 characters")

    def validate_full_name(self, value):
        """validation for username"""

        if value == "":
            raise serializers.ValidationError("full name cannot be empty")

    def validation(self, value):
        """validation for username"""

        if not any(character.isdigit() for character in value):
            raise serializers.ValidationError("passworrd must contain a number")
        if not any(character in "*/-+.&%^$#!_:;'" for character in value):
            raise serializers.ValidationError(
                "password must any of the special character"
            )
        if not any(character.isalpha for character in value):
            raise serializers.ValidationError("password must contain a capital word")
