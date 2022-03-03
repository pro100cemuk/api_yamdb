import jwt
from django.db import models
from django.contrib.auth.models import AbstractUser

from api_yamdb import settings

ROLE_CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='Роль'
    )

    class Meta:
        verbose_name = 'Пользователь'

    def __str__(self):
        return self.username

    def _generate_jwt_token(self):
        token = jwt.encode({
            'id': self.pk
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_user(self):
        return self.role == 'user'
