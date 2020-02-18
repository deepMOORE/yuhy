from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


class EventView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)

        # todo: create enum with three statuses
        # todo: create response model
        return Response(data={
            'status': status.HTTP_200_OK,
            'message': None,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

