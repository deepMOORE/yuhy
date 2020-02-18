from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from authentication.views import RegistrationView
from events.views import EventView

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^events/get-list/', EventView.as_view({'get': 'list'})),

    url(r'^user-register/', RegistrationView.as_view({'post': 'create'})),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
