from django.db import models


class Supplier(models.Model):
    id = models.IntegerField('organisasjonsnummer', primary_key=True)
    name = models.CharField('navn', max_length=200)
