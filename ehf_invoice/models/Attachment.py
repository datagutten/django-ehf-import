from django.db import models

from ehf_invoice.models import Invoice


class Attachment(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='attachments'
    )
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='invoice_attachments/%Y/')
    mime = models.CharField('MIME type', max_length=50)

    class Meta:
        unique_together = ['invoice', 'name']
        verbose_name = 'vedlegg'
        verbose_name_plural = 'vedlegg'
