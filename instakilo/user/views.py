"""temporary view system we view it later
    """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import Loginserializer
from user.serializers import Regsitrationclass


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

        serializer_class = Loginserializer
        print(request.data)

        serial = serializer_class(data=request.data)
        if serial.is_valid(raise_exception=True):
            print("valid data", serial.validated_data)
            return Response(
                data={"success": True, "data": request.data}, status=status.HTTP_200_OK
            )


class Registeration(APIView):
    """creating regdistration for user"""

    def post(self, request):
        """post function for the class registration

        Args:
            request (_type_): _description_
        """
        register = Regsitrationclass
        print(request.data)

        registering_data = register(data=request.data)
        if registering_data.is_valid(raise_exception=True):
            print("valid data", registering_data.validated_data)
            return Response(
                data={"success": True, "data": request.data}, status=status.HTTP_200_OK
            )
