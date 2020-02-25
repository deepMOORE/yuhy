from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Event, EventUser
from .serializers import EventSerializer, EventUserSerializer


class GetEventsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)

        # todo: create enum with three statuses
        # todo: create response model
        return Response(data={
            'status': 'success',
            'message': None,
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class CreateEventView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({
                'status': 'failed',
                'message': e.detail,
                'data': None,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            'status': 'success',
            'message': None,
            'data': None,
        }, status=status.HTTP_200_OK)


class EventParticipationView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventUserSerializer

    def register(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            event_id = serializer.validated_data['event_id']

            is_already_registered = EventUser.objects.filter(user_id=user_id, event_id=event_id)

            if not is_already_registered:
                serializer.save()

                return Response({
                    'status': 'success',
                    'message': None,
                    'data': None,
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'failed',
                    'message': 'User already participated in this event.',
                    'data': None,
                }, status=status.HTTP_400_BAD_REQUEST)
