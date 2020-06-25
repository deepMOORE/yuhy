from django.conf.urls import url
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from authentication.views import RegistrationView, LoginReturnTokenView
from comments.views import CreateCommentView
from events.views import GetEventsView, CreateEventView, EventParticipationView
from users.views import GetUserView, GetByEventIdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^events/get-list/', GetEventsView.as_view({'get': 'list'})),
    url(r'^events/create-event/', CreateEventView.as_view({'post': 'create'})),
    url(r'^events/register-user/', EventParticipationView.as_view({'post': 'register'})),
    url(r'^users/get-users-by-event-id/', GetByEventIdView.as_view({'post': 'list'})),

    url(r'^user/register/', RegistrationView.as_view({'post': 'create'})),
    url(r'^user/get-by-id/(?P<id>.+)/$', GetUserView.as_view({'get': 'get_by_id'})),

    url(r'^comments/create/', CreateCommentView.as_view({'post': 'create'})),

    url(r'^api-token-auth/', LoginReturnTokenView.as_view()),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
