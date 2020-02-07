from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
