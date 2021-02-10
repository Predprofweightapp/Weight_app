from django.db import models


class UserData(models.Model):
    login = models.EmailField('mail')
    password = models.CharField('password', max_length=10)