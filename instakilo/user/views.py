"""temporary view system we view it later
    """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import UserModel


from user.serializers import LoginSerializer
from user.serializers import RegsitrationSerializer


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
        register = RegsitrationSerializer
        print(request.data)

        registering_data = register(data=request.data)
        if registering_data.is_valid(raise_exception=True):
            print("valid data", registering_data.validated_data)

        user_obj = UserModel.objects.create(
            username=registering_data.validated_data.get("username"),
            first_name=registering_data.validated_data.get("first_name"),
            last_name=registering_data.validated_data.get("last_name"),
            email=registering_data.validated_data.get("email_id"),
        )

        return Response(
            data={
                "success": True,
                "username": user_obj.username,
                "email": user_obj.email,
            },
            status=status.HTTP_200_OK,
        )
