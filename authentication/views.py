from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.serializers import RegistrationSerializer
from users.models import User


class RegistrationView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': None,
            'data': serializer.data,
        }, status=status.HTTP_201_CREATED)
