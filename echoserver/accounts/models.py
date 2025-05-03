from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )

    email = models.CharField(
        max_length=254,
        blank=False,
        unique=True,
        error_messages={'unique': 'Этот email уже занят'}
    )
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    class Meta:
        swappable = 'AUTH_USER_MODEL'


    def __str__(self):
        return self.username

    def is_admin(self):
        return self.role == 'admin'