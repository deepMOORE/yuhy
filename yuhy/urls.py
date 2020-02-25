from django.conf.urls import url
# from django.contrib import admin
# from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from authentication.views import RegistrationView, LoginReturnTokenView
from events.views import GetEventsView, CreateEventView, EventParticipationView
from users.views import GetUserView

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^events/get-list/', GetEventsView.as_view({'get': 'list'})),
    url(r'^events/create-event/', CreateEventView.as_view({'post': 'create'})),
    url(r'^events/register-user/', EventParticipationView.as_view({'post': 'register'})),

    url(r'^user/register/', RegistrationView.as_view({'post': 'create'})),
    url(r'^user/get-by-id/(?P<id>.+)/$', GetUserView.as_view({'get': 'get_by_id'})),

    url(r'^api-token-auth/', LoginReturnTokenView.as_view()),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
