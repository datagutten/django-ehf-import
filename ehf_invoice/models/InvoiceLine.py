from django.db import models

from . import Invoice


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='lines'
    )
    line_id = models.IntegerField()

    description = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    quantity = models.IntegerField()
    sum = models.DecimalField(decimal_places=2, max_digits=12)

    class Meta:
        unique_together = ['invoice', 'line_id']
        verbose_name = 'fakturalinje'
        verbose_name_plural = 'fakturalinjer'

    def __str__(self):
        return '%s line %s %s' % (self.invoice, self.line_id, self.name)

    def invoice_number(self):
        return self.invoice.invoice_number
