from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    SEX_MALE = 'male'
    SEX_FEMALE = 'female'
    SEX_OTHER = 'other'

    SEX_CHOICE = (
        (SEX_MALE, 'Мужской'),
        (SEX_FEMALE, 'Женский'),
        (SEX_OTHER, 'Не указан'),
    )

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
    sex = models.CharField(max_length=6, choices=SEX_CHOICE, default=SEX_OTHER, verbose_name='Пол')
