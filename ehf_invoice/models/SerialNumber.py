from django.db import models

from . import InvoiceLine


class SerialNumber(models.Model):
    line = models.ForeignKey(
        InvoiceLine, on_delete=models.CASCADE, related_name='serials'
    )
    serial = models.CharField(primary_key=True, max_length=50)

    class Meta:
        unique_together = ['line', 'serial']

    def __str__(self):
        return self.serial
