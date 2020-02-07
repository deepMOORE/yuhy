from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
