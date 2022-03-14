import requests
from django.core.management import BaseCommand

from ehf_invoice.models import Supplier


class Command(BaseCommand):
    def handle(self, *args, **options):
        for supplier in Supplier.objects.filter(name='Ukjent'):
            if len(str(supplier.id)) != 9:
                continue
            response = requests.get(
                'https://data.brreg.no/enhetsregisteret/api/enheter/%s' % supplier.id)
            if response.status_code == 404:
                continue
            supplier.name = response.json()['navn']
            supplier.save()
