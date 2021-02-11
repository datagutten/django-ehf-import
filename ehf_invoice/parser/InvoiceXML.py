from base64 import b64decode
from decimal import Decimal
from xml.etree import ElementTree

from ehf_invoice.parser import Attachment
from ehf_invoice.parser.InvoiceLine import InvoiceLine
from ehf_invoice.parser.Party import Party


class InvoiceXML:
    namespaces = {
        'cac': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonBasicComponents-2',
    }

    invoice = None

    def __init__(self, file):
        # import xml.etree.ElementTree
        f = open(file, 'r')
        self.invoice = ElementTree.fromstring(f.read())
        f.close()

    def find(self, match):
        """

        :param str match:
        :return Element:
        """
        return self.invoice.find(match, self.namespaces)

    @property
    def invoice_number(self):
        return self.find('cbc:ID').text

    @property
    def invoice_date(self):
        return self.find('cbc:IssueDate').text

    @property
    def customer(self):
        customer = self.find('cac:AccountingCustomerParty/cac:Party')
        return Party(customer)

    @property
    def supplier(self):
        supplier = self.find('cac:AccountingSupplierParty/cac:Party')
        return Party(supplier)

    # @property
    # def supplier_name(self):
    #     return (
    #         self.supplier
    #             .find('cac:PartyName/cbc:Name', self.namespaces)
    #             .text
    #     )

    @property
    def order_reference(self):
        reference = self.find('cac:OrderReference/cbc:ID')
        if reference:
            return reference

    @property
    def order_number(self):
        objects = self.invoice.findall(
            'cac:ContractDocumentReference/cbc:ID', self.namespaces
        )
        references = []
        reference1 = self.order_reference
        for reference in objects:
            if not reference.text == reference1:
                return reference.text
            # references.append(reference.text)
        # return references

    def attachments(self):
        objects = self.invoice.findall('cac:AdditionalDocumentReference/cac:Attachment', self.namespaces)
        attachments = []
        for att in objects:
            attachments.append(Attachment(att))
        return attachments

    @property
    def amount(self):
        return Decimal(
            self.find('cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount').text
        )

    def invoice_lines(self):
        lines_xml = self.invoice.findall('cac:InvoiceLine', self.namespaces)
        lines = []
        for line in lines_xml:
            lines.append(InvoiceLine(line))
        return lines
