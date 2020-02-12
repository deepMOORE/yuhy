from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        return Response(data=None, status=status.HTTP_200_OK)
