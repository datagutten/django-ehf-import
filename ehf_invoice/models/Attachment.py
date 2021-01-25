from django.db import models

from ehf_invoice.models import Invoice


class Attachment(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='attachments'
    )
    file = models.FileField(upload_to='invoice_attachments/%Y/')
    mime = models.CharField('MIME type', max_length=50)

    class Meta:
        unique_together = ['invoice', 'file']
