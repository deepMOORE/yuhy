from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from authentication.views import RegistrationView, LoginReturnTokenView
from events.views import EventView
from users.views import GetUserView

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^events/get-list/', EventView.as_view({'get': 'list'})),

    url(r'^user/register/', RegistrationView.as_view({'post': 'create'})),
    url(r'^user/get-by-id/(?P<id>.+)/$', GetUserView.as_view({'get': 'get_by_id'})),

    url(r'^api-token-auth/', LoginReturnTokenView.as_view()),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
