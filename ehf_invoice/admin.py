from django.contrib import admin

from ehf_invoice.models import Invoice, InvoiceLine, SerialNumber


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'invoice_number', 'date']
    readonly_fields = ['invoice_lines']


@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'line_id', 'name']
    list_filter = ['invoice']


@admin.register(SerialNumber)
class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ['line', 'serial']
    list_filter = ['line__invoice']
