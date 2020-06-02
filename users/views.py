from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from django.db import connection
from users.serializers import UserSerializer


class GetUserView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['id'])

    def get_by_id(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data={
            'status': 'success',
            'message': None,
            'data': {
                'user': serializer.data[0]
            }
        }, status=status.HTTP_200_OK)


class GetByEventIdView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        event_id = request.data.get('id')
        cursor = connection.cursor()
        cursor.execute('select uu.username '
                       'from events_eventuser '
                       'join users_user uu on events_eventuser.user_id_id = uu.id '
                       'join events_event ee on events_eventuser.event_id_id = ee.id '
                       'where ee.id = ' + str(event_id))
        data = cursor.fetchall()

        return Response(data={
            'status': 'success',
            'message': None,
            'data': data
        }, status=status.HTTP_200_OK)
