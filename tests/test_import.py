import os
import datetime

from django.test import TestCase
from ehf_invoice.management.commands.load_invoice import Command
from ehf_invoice.models import Invoice


class ImportTestCase(TestCase):
    def testImport(self):
        file = os.path.join(os.path.dirname(__file__), 'test_data',
                            'T10 BII05 gyldig faktura.xml')
        load = Command()
        load.load(file)
        invoice = Invoice.objects.get(invoice_number='TOSL108')
        self.assertIsInstance(invoice, Invoice)
        self.assertEqual(datetime.date(2013, 6, 30), invoice.date)
        self.assertEqual('TOSL108', invoice.invoice_number)
        self.assertEqual('Contract321', invoice.order_number)
