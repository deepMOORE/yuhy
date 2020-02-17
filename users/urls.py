from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register('users', views.UserView)

urlpatterns = [
    url(r'create/', include(router.urls)),
]
