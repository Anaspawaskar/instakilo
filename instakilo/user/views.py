"""temporary view system we view it later
    """


import os
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import UserModel
import jwt


from user.serializers import LoginSerializer
from user.serializers import RegsitrationSerializer


class Registeration(APIView):
    """creating regdistration for user"""

    def post(self, request):
        """post function for the class registration

        Args:
            request (_type_): _description_
        """
        serializer_class = RegsitrationSerializer
        print(request.data)

        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("valid data", serializer.validated_data)
            try:
                user_obj = UserModel.objects.create(
                    username=serializer.validated_data.get("username"),
                    first_name=serializer.validated_data.get("first_name"),
                    last_name=serializer.validated_data.get("last_name"),
                    email=serializer.validated_data.get("email_id"),
                )
                user_obj.set_password(serializer.validated_data.get("password"))
                user_obj.save()

                return Response(
                    data={
                        "success": True,
                        "username": user_obj.username,
                        "email": user_obj.email,
                    },
                    status=status.HTTP_200_OK,
                )

            except IntegrityError:
                return Response(
                    data={
                        "success": False,
                        "message": "username or email already exists",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )


class Login(APIView):
    """this class id for the login page"""

    def post(self, request):
        """post function for the class login

        Args:
            request (_type_): _description_
            format (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """

        serializer_class = LoginSerializer
        print(request.data)

        serial = serializer_class(data=request.data)

        if serial.is_valid(raise_exception=True):
            print("valid data", serial.validated_data)

        try:
            user = authenticate(
                username=serial.validated_data.get("username"),
                password=serial.validated_data.get("password"),
            )
            print(user)

            encoded_jwt = jwt.encode(
                {"username": serial.validated_data.get("username")},
                "secret",
                algorithm=os.environ.get("DB_algorithm"),
            )
            print(encoded_jwt)

            if user is not None:
                return Response(
                    data={"success": True, "data": request.data},
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data={
                        "success": False,
                        "message": "username and password does not match",
                    },
                    status=status.HTTP_200_OK,
                )

        except ValueError:
            return Response(
                data={
                    "success": False,
                    "verror": "username and password odes not matched",
                }
            )
