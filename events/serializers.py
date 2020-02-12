from rest_framework import serializers
from .models import Event, EventUser


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'country_id', 'event_date')


class EventUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUser
        fields = ('user_id', 'event_id')
