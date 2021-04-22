from decimal import Decimal
from xml.etree import ElementTree

from ehf_invoice.parser import Attachment, CreditNoteLine, InvoiceLine, Party


class InvoiceXML:
    namespaces = {
        'cac': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonBasicComponents-2',
    }

    invoice = None

    def __init__(self, file):
        f = open(file, 'r')
        self.invoice = ElementTree.fromstring(f.read())
        if self.invoice.tag == '{urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2}CreditNote':
            self.credit = True
        else:
            self.credit = False

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
        objects = self.invoice.findall(
            'cac:AdditionalDocumentReference/cac:Attachment', self.namespaces)
        attachments = []
        for att in objects:
            try:
                attachments.append(Attachment(att))
            except ValueError:
                continue
        return attachments

    @property
    def amount(self):
        value = Decimal(
            self.find('cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount').text
        )
        if self.credit:
            return -value
        else:
            return value

    def invoice_lines(self):
        if self.credit:
            lines_xml = self.invoice.findall('cac:CreditNoteLine',
                                             self.namespaces)
        else:
            lines_xml = self.invoice.findall('cac:InvoiceLine',
                                             self.namespaces)
        lines = []
        for line in lines_xml:
            if self.credit:
                lines.append(CreditNoteLine(line))
            else:
                lines.append(InvoiceLine(line))
        return lines
