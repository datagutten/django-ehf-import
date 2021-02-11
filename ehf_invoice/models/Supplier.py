from django.db import models


class Supplier(models.Model):
    id = models.IntegerField('organisasjonsnummer', primary_key=True)
    name = models.CharField('navn', max_length=200)

    class Meta:
        verbose_name = 'leverandør'
        verbose_name_plural = 'leverandører'

    def __str__(self):
        return self.name
