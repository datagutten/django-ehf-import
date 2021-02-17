from base64 import b64decode


class Attachment:
    namespaces = {
        'cac': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:'
               'ubl:schema:xsd:CommonBasicComponents-2',
    }

    def __init__(self, element):
        self.element = element

        file = element.find('cbc:EmbeddedDocumentBinaryObject',
                            self.namespaces)
        if file is None:
            raise ValueError('No file in attachment')
        if 'filename' not in file.attrib:
            raise ValueError('Attachment has no file name')

        self.file_name = file.attrib['filename']
        self.mime = file.attrib['mimeCode']

        if 'format' not in file.attrib or file.attrib['format'] == 'BASE64':
            self.data = b64decode(file.text, validate=True)
        else:
            raise ValueError(
                'Unknown attachment format: %s' % file.attrib['format'])
