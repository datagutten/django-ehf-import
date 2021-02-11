from django.db import models

from . import InvoiceLine


class SerialNumber(models.Model):
    line = models.ForeignKey(
        InvoiceLine, on_delete=models.CASCADE, related_name='serials',
        verbose_name='fakturalinje'
    )
    serial = models.CharField(primary_key=True, max_length=50,
                              verbose_name='serienummer')

    class Meta:
        unique_together = ['line', 'serial']
        verbose_name = 'serienummer'
        verbose_name_plural = 'serienummer'

    def __str__(self):
        return self.serial
