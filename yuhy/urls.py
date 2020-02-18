from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from authentication import views as auth_views
from events import views as event_views

router = routers.DefaultRouter()
router.register('auth', auth_views.RegistrationView)
router.register('events', event_views.EventView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/', include(router.urls)),
    url(r'^get/', include(router.urls)),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
