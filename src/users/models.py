from django.db import models
from django.contrib.auth import models as auth_models

class ExtUserData(models.Model):
    user = models.OneToOneField(
        auth_models.User,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name='Пользватель'
    )
    
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=80,
        blank=True,
        default=''
    )
    
    country = models.CharField(
        verbose_name='Страна',
        max_length=80,
        blank=True,
        default='Беларусь'
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=80,
        blank=True,
        default=''
    )

    post_index = models.CharField(
        verbose_name='Почтовый индекс',
        max_length=80,
        blank=True,
        default=''
    )

    address1 = models.CharField(
        verbose_name='Адрес 1',
        max_length=120,
        blank=True,
        default=''
    )

    address2 = models.CharField(
        verbose_name='Адрес 2',
        max_length=120,
        blank=True,
        default=''
    )

    def __str__(self):
        return f'{self.phone}, {self.address1},  {self.address2},  {self.post_index},  {self.city}, {self.country}'
