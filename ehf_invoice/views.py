from django.shortcuts import render

from ehf_invoice.models import Invoice, SerialNumber


def show_invoice(request, invoice_number):
    invoice = Invoice.objects.get(invoice_number=invoice_number)
    return render(request, 'ehf_invoice/invoice.html', {'invoice': invoice})


def find_serial(request, serial_number):
    serial = SerialNumber.objects.get(serial=serial_number)
    invoice = serial.item.invoice
    return render(request, 'ehf_invoice/invoice.html', {'invoice': invoice})
