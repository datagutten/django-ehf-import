from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from ehf_invoice.models import Invoice, SerialNumber


@permission_required('ehf_invoice.view_invoice', raise_exception=True)
def show_invoice(request, invoice_number):
    invoice = Invoice.objects.get(invoice_number=invoice_number)
    return render(request, 'ehf_invoice/invoice.html', {'invoice': invoice})


@permission_required('ehf_invoice.view_serialnumber', raise_exception=True)
def find_serial(request, serial_number):
    serial = SerialNumber.objects.get(serial=serial_number)
    invoice = serial.line.invoice
    return render(request, 'ehf_invoice/invoice.html', {'invoice': invoice})
