from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from users.models import User
from django.db import connection
from users.serializers import UserSerializer


class GetUserView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['id'])

    def get_by_id(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute(
            'select u.*, ee.* from users_user as u left join events_eventuser as eeu on eeu.user_id_id = u.id left join events_event as ee on ee.id = eeu.event_id_id where u.id = ' + self.kwargs['id'])
        data = cursor.fetchall()
        return Response(data={
            'status': 'success',
            'message': None,
            'data': {
                'user': data
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
