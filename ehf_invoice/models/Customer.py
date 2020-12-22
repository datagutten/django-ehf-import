from django.db import models


class Customer(models.Model):
    id = models.IntegerField('organisasjonsnummer', unique=True)
    name = models.CharField('navn', max_length=200)
