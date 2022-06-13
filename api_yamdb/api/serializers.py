from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                {'username': ['Invalid username: me']})
        return data


class TokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
    token = serializers.ReadOnlyField()

    def validate(self, data):
        user = get_object_or_404(User, username=data.get('username'))
        try:
            refresh = RefreshToken(data.get('confirmation_code'))
        except TokenError as error:
            raise serializers.ValidationError(
                {'confirmation_code': error})
        if user.id != refresh.payload.get('user_id'):
            raise serializers.ValidationError(
                {'error': ['Wrong username or code']})
        return {'token': str(refresh.access_token)}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'bio', 'email', 'role',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'bio', 'email', 'role',)
        read_only_fields = ('role', )
