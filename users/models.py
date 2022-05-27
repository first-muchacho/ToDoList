from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    email = models.EmailField('email address', unique=True)
    email_verify = models.BooleanField(default=False)
    gender = models.CharField('Gender', max_length=1, choices=GENDER, default='')
    birth_date = models.DateField('Birthdate', null=True)
