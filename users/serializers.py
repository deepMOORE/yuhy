from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'created_at',
            'password')
        extra_kwargs = {'password': {'write_only': True}}
