from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from ehf_invoice.models import Invoice, SerialNumber, Supplier


@permission_required('ehf_invoice.view_supplier', raise_exception=True)
def show_supplier(request, supplier):
    supplier = Supplier.objects.get(id=supplier)
    return render(request, 'ehf_invoice/supplier.html', {'supplier': supplier})


@permission_required('ehf_invoice.view_invoice', raise_exception=True)
def show_invoice(request, invoice_number=None):
    if not invoice_number:
        if request.GET.get('id'):
            invoice = Invoice.objects.get(id=request.GET.get('id'))
        else:
            raise ValueError('No invoice identifier set')
    else:
        invoice = Invoice.objects.get(invoice_number=invoice_number)
    return render(request, 'ehf_invoice/invoice.html', {'invoice': invoice})


@permission_required('ehf_invoice.view_serialnumber', raise_exception=True)
def find_serial(request, serial_number):
    serial = SerialNumber.objects.get(serial=serial_number)
    invoice = serial.line.invoice
    return render(request, 'ehf_invoice/invoice.html', {'invoice': invoice})
