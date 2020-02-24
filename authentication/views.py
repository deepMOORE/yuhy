from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from authentication.serializers import RegistrationSerializer
from users.models import User
from yuhy.response_handlers import jwt_response_payload_handler


class RegistrationView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({
                'status': 'failed',
                'message': e.detail,
                'data': None,
            }, status=status.HTTP_201_CREATED)

        serializer.save()

        return Response({
            'status': 'success',
            'message': None,
            'data': serializer.data,
        }, status=status.HTTP_201_CREATED)


class LoginReturnTokenView(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
