from django import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=8, help_text='Статус заявки')  # Statuses: pending/approved/signed/rejected

    def str(self):
        return self.name


class Credit(models.Model):
    sum = models.IntegerField(help_text='Сумма кредита')
    currency = models.CharField(max_length=1, help_text='Валюта')
    user = models.ForeinKey('Client', on_delete=models.PROTECT,
                            help_text='Валюта')
    status = models.ForeignKey('Status', on_delete=models.PROTECT)

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания заявки')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_active = models.BooleanField(default=True)

class Client(models.Model):
    # Full client name
    name = models.CharField(max_length=50, help_text='Имя клиента')
    patronymic = models.CharField(max_length=50, help_text='Отчество клиента')
    surname = models.CharField(max_length=50, help_text='Фамилия клиента')

    # Passport
    passport_seria = models.CharField(max_length=2, help_text='Серия паспорта клиента')
    pasport_id = models.IntegerField(help_text='Номер паспорта клиента')

    # location
    location = models.CharField(max_length=50, help_text='Место жительства клиента')
    country = CountryField(help_text='Страна проживания клиента')
    city = models.CharField(max_length=50, help_text='Город проживания клиента')
    street = models.CharField(max_length=50, help_text='Улица проживания клиента')
    house_number = models.CharField(max_length=50, help_text='Номер дома клиента')
    apartnent_number = models.CharField(max_length=50, help_text='Номер квартиры клиента')

    # contacts
    email = models.CharField(max_length=50, help_text='Эл.почта клиента')
    phone_number = models.IntegerField(help_text='Номер телефона клиента')

    # auntification


    # default values
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_active = models.BooleanField(default=True)


class Administrator(models.Model):
    # Full admin name
    name = models.CharField(max_length=50, help_text='Имя администратора')
    patronymic = models.CharField(max_length=50, help_text='Отчество администратора')
    surname = models.CharField(max_length=50, help_text='Фамилия администратора')

    # auntification


    # default values
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_active = models.BooleanField(default=True)