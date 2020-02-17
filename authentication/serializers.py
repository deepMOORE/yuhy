from rest_framework import serializers
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=6
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
