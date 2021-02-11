import os
import unittest

from ehf_invoice.parser import InvoiceXML, Party


class ParserTestCase(unittest.TestCase):
    def test_parser(self):
        invoice = InvoiceXML(
            os.path.join(os.path.dirname(__file__), 'test_data',
                         'T10 BII05 gyldig faktura.xml'))
        self.assertEqual(1436.5, invoice.amount)
        self.assertIsInstance(invoice.customer, Party)
        self.assertIsInstance(invoice.supplier, Party)
        self.assertEqual('2013-06-30', invoice.invoice_date)
        self.assertEqual('TOSL108', invoice.invoice_number)
        self.assertEqual('Contract321', invoice.order_number)


if __name__ == '__main__':
    unittest.main()
