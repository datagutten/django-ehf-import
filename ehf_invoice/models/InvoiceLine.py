from django.db import models

from . import Invoice


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='lines',
        verbose_name='faktura'
    )
    line_id = models.IntegerField('linje')

    description = models.CharField('beskrivelse', max_length=300, null=True,
                                   blank=True)
    name = models.CharField('navn', max_length=300)
    price = models.DecimalField('beløp', decimal_places=2, max_digits=12)
    quantity = models.IntegerField('antall')
    sum = models.DecimalField('sum', decimal_places=2, max_digits=12)

    class Meta:
        unique_together = ['invoice', 'line_id']
        verbose_name = 'fakturalinje'
        verbose_name_plural = 'fakturalinjer'
        ordering = ['invoice', 'line_id']

    def __str__(self):
        return '%s line %s %s' % (self.invoice, self.line_id, self.name)

    def invoice_number(self):
        return self.invoice.invoice_number
