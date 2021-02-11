class Party:
    namespaces = {
        'cac': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonBasicComponents-2',
    }

    def __init__(self, element):
        self.id = element.find('cbc:EndpointID', self.namespaces).text
        self.name = element.find('cac:PartyName/cbc:Name', self.namespaces).text
