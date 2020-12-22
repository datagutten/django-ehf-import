from django.db import models
from django.db.models import UniqueConstraint

from . import Invoice


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='lines'
    )
    line_id = models.IntegerField()

    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    sum = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['invoice', 'line_id'], name='unique_invoice_line_id'
            )
        ]

    def __str__(self):
        return '%s line %s %s' % (self.invoice, self.line_id, self.name)

    def invoice_number(self):
        return self.invoice.invoice_number