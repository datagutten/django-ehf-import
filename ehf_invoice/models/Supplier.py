from django.db import models


class Supplier(models.Model):
    id = models.IntegerField('organisasjonsnummer', unique=True)
    name = models.CharField('navn', max_length=200)
