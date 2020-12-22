class InvoiceLine:
    line = None
    namespaces = {
        'cac': 'urn:oasis:names:specification:ubl:'
        'schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:ubl:'
        'schema:xsd:CommonBasicComponents-2',
    }

    def __init__(self, line):
        self.line = line

    def id(self):
        return self.line.find('cbc:ID', self.namespaces).text

    def quantity(self):
        q = self.line.find('cbc:InvoicedQuantity', self.namespaces).text
        # q = q[:-3]
        return int(float(q))

    def description(self):
        return self.line.find('cac:Item/cbc:Description', self.namespaces).text

    def name(self):
        return self.line.find('cac:Item/cbc:Name', self.namespaces).text

    def serials(self):
        properties = self.line.findall(
            'cac:Item/cac:AdditionalItemProperty/'
            'cbc:Name[.="SerialNumber"]/../cbc:Value',
            self.namespaces,
        )
        serials = []
        for serial in properties:
            serials.append(serial.text)
        return serials

    def price(self):
        """
        Price of one item
        :return:
        """
        return float(
            self.line.find('cac:Price/cbc:PriceAmount', self.namespaces).text
        )

    def sum(self):
        """
        Sum of the line
        :return:
        """
        return float(
            self.line.find('cbc:LineExtensionAmount', self.namespaces).text
        )
