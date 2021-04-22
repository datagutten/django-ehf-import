import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from ehf_invoice.models import (
    Invoice,
    InvoiceLine,
    SerialNumber,
    Attachment,
    Supplier,
    Customer,
)
from ehf_invoice.parser import InvoiceXML


class Command(BaseCommand):
    help = 'Load invoice'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def load(self, file: str) -> Invoice:
        invoice = InvoiceXML(file)
        supplier_xml = invoice.supplier
        supplier, created = Supplier.objects.get_or_create(
            id=supplier_xml.id, defaults={'name': supplier_xml.name}
        )

        customer, created = Customer.objects.get_or_create(
            id=invoice.customer.id, defaults={'name': invoice.customer.name}
        )

        try:
            invoice_obj = Invoice.objects.get(
                supplier=supplier, invoice_number=invoice.invoice_number
            )
        except Invoice.DoesNotExist:
            invoice_obj = Invoice(
                supplier=supplier, invoice_number=invoice.invoice_number
            )

        invoice_obj.customer = customer
        invoice_obj.order_number = invoice.order_number
        invoice_obj.date = invoice.invoice_date
        invoice_obj.amount = invoice.amount
        invoice_obj.credit = invoice.credit

        invoice_obj.save()
        print(invoice_obj)

        for attachment in invoice.attachments():
            try:
                Attachment.objects.get(
                    invoice=invoice_obj, name=attachment.file_name
                )
                continue
            except Attachment.DoesNotExist:
                file = ContentFile(attachment.data)
                file.name = attachment.file_name
                attachment_obj = Attachment(
                    invoice=invoice_obj,
                    mime=attachment.mime,
                    file=file,
                    name=attachment.file_name,
                )
                attachment_obj.save()

        for line in invoice.invoice_lines():
            line_obj, created = InvoiceLine.objects.get_or_create(
                invoice=invoice_obj,
                line_id=line.id,
                defaults={
                    'quantity': line.quantity,
                    'description': line.description,
                    'name': line.name,
                    'price': line.price,
                    'sum': line.sum,
                },
            )
            if line_obj.sum != line.sum:
                line_obj.quantity = line.quantity
                line_obj.description = line.description
                line_obj.name = line.name
                line_obj.price = line.price
                line_obj.sum = line.sum
                line_obj.save()

            for serial in line.serials:
                serial_obj = SerialNumber(line=line_obj, serial=serial)
                serial_obj.save()
        return invoice_obj

    def handle(self, *args, **options):
        if os.path.isfile(options['file'][0]):
            self.load(options['file'][0])
        elif os.path.isdir(options['file'][0]):
            for file in os.scandir(options['file'][0]):
                if os.path.isfile(file):
                    self.load(file)
