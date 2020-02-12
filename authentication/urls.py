from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^users/?$', view=views.register, name='register'),
]
