from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer


class GetUserView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['id'])

    def get_by_id(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data={
            'status': 'success',
            'message': None,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
