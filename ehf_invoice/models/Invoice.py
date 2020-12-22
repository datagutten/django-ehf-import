from django.db import models

from ehf_invoice.models import Supplier, Customer


class Invoice(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, verbose_name='leverandør'
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name='kunde'
    )
    invoice_number = models.CharField(primary_key=True, max_length=100)
    order_number = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return '%s invoice %s' % (self.supplier, self.invoice_number)

    def invoice_lines(self):
        return self.lines.all()