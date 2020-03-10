from rest_framework import serializers
from .models import Event, EventUser


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'event_date', 'description', 'latitude', 'longitude']


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ['user_id', 'event_id']


class EventFromUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ['event_id']



