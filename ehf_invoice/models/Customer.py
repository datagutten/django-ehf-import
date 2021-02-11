from django.db import models


class Customer(models.Model):
    id = models.IntegerField('organisasjonsnummer', primary_key=True)
    name = models.CharField('navn', max_length=200)

    class Meta:
        verbose_name = 'kunde'
        verbose_name_plural = 'kunder'

    def __str__(self):
        return self.name
