from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
import random,string

# Create Your Models Here

class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, username = ''.join(random.choice(string.ascii_lowercase) for i in range(8)),**extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    alphabatic = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')
    numeric = RegexValidator(r'^[0-9]*$', 'Only numerics are allowed.')
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'alphanumeric are allowed.')

   
    username = models.CharField('User_name', max_length=255, blank=True)
    email = models.EmailField('Email Address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True, validators=[alphabatic], null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True, validators=[alphabatic], null=False)
    date_of_birth = models.DateField('DOB', blank=True, null=False)
    # phone = models.IntegerField('Phone Number', max_length=10, validators=[numeric], null=True)
    # must needed, otherwise you won't be able to log-in to django-admin
    is_staff = models.BooleanField(default=True)

    # must needed, otherwise you won't be able to log-in to django-admin
    is_active = models.BooleanField(default=True)
              # models.CharField(unique=True, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()