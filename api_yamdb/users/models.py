from django.contrib.auth.models import (AbstractUser,
                                        PermissionsMixin,
                                        BaseUserManager)
from django.db import models
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name='', last_name='', bio='',
                    role='user', password=None):
        if email is None:
            raise ValueError('Users must have an email address')
        if username is None:
            raise ValueError('Users must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,  first_name='', last_name='',
                         bio='', role='admin', password=None):
        if password is None:
            raise ValueError('Users must have password')
        user = self.create_user(
            email,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            role=role
        )
        user.is_staff = True
        user.is_superuser = True
        user.role = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    role = models.CharField(
        max_length=40,
        choices=settings.USERS_ROLE,
        default='user',
        verbose_name='Роль пользователя'
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Email адрес'
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='О себе'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Активна'
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='Персонал'
    )

    is_superuser = models.BooleanField(
        default=False,
        verbose_name='Суперпользователь'
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username
