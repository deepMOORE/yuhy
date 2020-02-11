from django.urls import path, include
from events import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', views.EventView)

urlpatterns = [
    path('', include(router.urls))
]
