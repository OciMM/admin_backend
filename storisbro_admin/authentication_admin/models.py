from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(Permission, related_name='users')
    name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email' 
