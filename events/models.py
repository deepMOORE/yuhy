from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        validators=[MinValueValidator(-100.0), MaxValueValidator(100.0)],
        default=None,
        blank=True,
        null=True
    )
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        validators=[MinValueValidator(-100.0), MaxValueValidator(100.0)],
        default=None,
        blank=True,
        null=True
    )
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class EventUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
