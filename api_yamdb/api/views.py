from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import (
    UserCreateSerializer,
    TokenObtainSerializer,
    UserSerializer,
    ProfileSerializer
)
from .mixins import CreateViewSet, RetrievePatchViewSet
from .utils import send_confirmation_email
from .permissions import AdminPermission, OwnPermission

User = get_user_model()


class EmailConfirmationViewSet(CreateViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(
            username=request.data.get('username'),
            email=request.data.get('email')
        )
        if not user.exists():
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
        user = user[0]
        refresh = RefreshToken.for_user(user)
        send_confirmation_email(str(refresh), user.email)
        return Response(
            {
                'username': request.data.get('username'),
                'email': request.data.get('email')
            },
            status=status.HTTP_200_OK
        )


class ObtainTokenView(TokenRefreshView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AdminPermission,)
    lookup_field = 'username'
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)


class ProfileViewSet(RetrievePatchViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (OwnPermission,)
    queryset = User.objects.all()

    def get_object(self):
        obj = get_object_or_404(
            self.queryset,
            username=self.request.user.username
        )
        self.check_object_permissions(self.request, obj)
        return obj
