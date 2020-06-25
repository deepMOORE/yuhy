from django.db import models
from events.models import Event
from users.models import User


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
