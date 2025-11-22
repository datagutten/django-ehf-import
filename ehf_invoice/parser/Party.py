class Party:
    namespaces = {
        'cac': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonBasicComponents-2',
    }

    def __init__(self, element):
        self.id = element.find('cbc:EndpointID', self.namespaces).text
        if element.find('cac:PartyName/cbc:Name', self.namespaces) is not None:
            self.name = element.find('cac:PartyName/cbc:Name', self.namespaces).text
        elif element.find('cac:PartyLegalEntity/cbc:RegistrationName', self.namespaces) is not None:
            self.name = element.find('cac:PartyLegalEntity/cbc:RegistrationName', self.namespaces).text
        else:
            self.name = None
