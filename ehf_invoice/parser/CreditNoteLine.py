from . import InvoiceLine


class CreditNoteLine(InvoiceLine):
    @property
    def quantity(self):
        q = self.line.find('cbc:CreditedQuantity', self.namespaces).text
        return -int(float(q))

    @property
    def price(self):
        return -super(CreditNoteLine, self).price

    @property
    def sum(self):
        return -super(CreditNoteLine, self).sum
