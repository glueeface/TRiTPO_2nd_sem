from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=8, db_index=True, help_text='Статус заявки')  # Statuses: pending/approved/signed/rejected

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['name']

    def get_absolute_url(self):
         return reverse('status', kwargs={'status_id': self.name})

    def str(self):
        return self.name


class Credit(models.Model):

    sum = models.IntegerField(help_text='Сумма кредита')
    currency = models.CharField(max_length=1, help_text='Валюта')
    status = models.ForeignKey('Status', on_delete=models.PROTECT)

    user = models.ForeignKey('userProfile', on_delete=models.PROTECT, help_text='Владелец заявки', null=True)

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания заявки')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
         return reverse('credit', kwargs={'credit_id': self.status})

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['id']


class userProfile(models.Model):
    # Full client name + auntification
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    # Passport
    passport_seria = models.CharField(max_length=2, help_text='Серия паспорта клиента')
    pasport_id = models.IntegerField(help_text='Номер паспорта клиента', blank=True, null=True)

    # location
    country = CountryField(help_text='Страна проживания клиента')
    city = models.CharField(max_length=50, help_text='Город проживания клиента')
    street = models.CharField(max_length=50, help_text='Улица проживания клиента')
    house_number = models.CharField(max_length=50, help_text='Номер дома клиента')
    apartnent_number = models.CharField(max_length=50, help_text='Номер квартиры клиента')


    def __str__(self):
        return self.user.username


# class Administrator(models.Model):
#     # auntification
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
