from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER = (
        ('m', 'Мужчина'),
        ('f', 'Женщина')
    )
    email = models.EmailField('email address', unique=True)
    email_verify = models.BooleanField(default=False)
    gender = models.CharField('Пол', max_length=1, choices=GENDER, default='')
    birth_date = models.DateField('Дата рождения', default='2022-05-11')
