from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

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


@receiver(post_delete, sender=Attachment)
def attachment_delete(sender, instance: Attachment, **kwargs):
    """
    Receive the post_delete signal
    and delete the file associated with the model instance.
    https://stackoverflow.com/a/14310174/2630074
    """
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
