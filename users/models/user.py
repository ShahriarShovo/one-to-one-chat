from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from users.models.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    
    first_name      =   models.CharField(max_length=50, null=True, blank=True)
    last_name       =   models.CharField(max_length=50, null=True, blank=True)
    username        =   models.CharField(max_length=50, unique=True)
    email           =   models.EmailField(max_length=100, unique=True)
   
    # requires fields
    date_joined     =   models.DateTimeField(auto_now_add=True)
    last_login      =   models.DateTimeField(auto_now_add=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    modify_date     =   models.DateTimeField(auto_now=True)
    is_admin        =   models.BooleanField(default=False)
    is_staff        =   models.BooleanField(default=False)
    is_active       =   models.BooleanField(default=False)
    is_superuser    =   models.BooleanField(default=False)


    USERNAME_FIELD  =   'email'
    #REQUIRED_FIELDS =  ['email',]

    objects         =  UserManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

