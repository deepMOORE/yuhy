from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    country_id = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class EventUser(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
