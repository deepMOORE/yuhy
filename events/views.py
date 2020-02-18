from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import ValidationError
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
            'status': status.HTTP_200_OK,
            'message': None,
            'data': None,
        }, status=status.HTTP_201_CREATED)

