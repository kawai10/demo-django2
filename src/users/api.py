from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from src.users.serializers import CreateUserSerializer, LoginSerializer


class RegisterUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer


class LoginUserAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        res = super().post(request, *args, **kwargs)

        response = Response({"result": "login success"}, status=status.HTTP_200_OK)
        response.set_cookie(
            "refresh_token", res.data.get("refresh", None), httponly=True
        )
        response.set_cookie("access_token", res.data.get("access", None), httponly=True)

        return response


class TokenRefreshAPIView(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.COOKIES.get("refresh_token", None)
        data = {"refresh": refresh_token}
        token_serializer = self.get_serializer(data=data)

        try:
            token_serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        token = token_serializer.validated_data
        response = Response(
            {"detail": "token refresh success"}, status=status.HTTP_200_OK
        )
        response.set_cookie("access_token", token["access"], httponly=True)
        response.set_cookie("refresh_token", token["refresh"], httponly=True)

        return response


# class LoginUserAPIView(APIView):
#     @staticmethod
#     def post(request: Request) -> Response:
#         user = authenticate(
#             email=request.data["email"], password=request.data["password"]
#         )
#
#         if user is not None:
#             user_serializer = UserSerializer(user)
#
#             token = TokenObtainPairSerializer.get_token(user)
#
#             response = Response(user_serializer.data, status.HTTP_200_OK)
#
#             response.set_cookie("access_token", str(token.access_token), httponly=True)
#             response.set_cookie("refresh_token", str(token), httponly=True)
#
#             return response
#
#         return Response(status=status.HTTP_400_BAD_REQUEST)
