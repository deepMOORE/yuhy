from rest_framework import serializers
from .models import Event, EventUser


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'description', 'latitude', 'longitude']


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ['user_id', 'event_id']
