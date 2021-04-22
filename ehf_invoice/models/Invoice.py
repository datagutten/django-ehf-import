from django.db import models

from ehf_invoice.models import Supplier, Customer


class Invoice(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, verbose_name='leverandør',
        related_name='invoices'
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name='kunde',
        related_name='invoices'
    )
    invoice_number = models.CharField('fakturanummer', max_length=100)
    order_number = models.CharField('ordrenummer', max_length=100, blank=True,
                                    null=True)
    date = models.DateField('fakturadato')
    amount = models.DecimalField('beløp', decimal_places=2, max_digits=12)
    credit = models.BooleanField('kreditnota', default=False)

    class Meta:
        unique_together = ['supplier', 'invoice_number']
        verbose_name = 'faktura'
        verbose_name_plural = 'fakturaer'
        ordering = ['-date']

    def __str__(self):
        return '%s invoice %s' % (self.supplier, self.invoice_number)

    def invoice_lines(self):
        return self.lines.all()
