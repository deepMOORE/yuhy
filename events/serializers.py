from rest_framework import serializers
from .models import Event


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'country_id', 'event_date')

    def create(self, validated_data):
        return super().create(validated_data)
