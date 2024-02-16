from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import(
    hello, 
    register_user
)


urlpatterns = [
    path('hello/', hello),

    # REGISTER
    path('api/register/', register_user, name='register_user'),
    # GET TOKEN
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
