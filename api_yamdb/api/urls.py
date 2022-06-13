from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    ObtainTokenView,
    EmailConfirmationViewSet,
    UserViewSet,
    ProfileViewSet
)

router = DefaultRouter()
router.register('auth/signup', EmailConfirmationViewSet, basename='signup')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/token/', ObtainTokenView.as_view(), name='token'),
    path(
        "v1/users/me/",
        ProfileViewSet.as_view(
            {"patch": "partial_update", "get": "retrieve"}
        ),
        name="profile-retrieve-update",
    ),
    path('v1/', include(router.urls)),
]
