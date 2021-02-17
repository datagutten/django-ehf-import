from django.contrib import admin

from ehf_invoice.models import Invoice, InvoiceLine, SerialNumber, \
    Attachment, Customer, Supplier


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_filter = ['supplier']
    list_display = ['supplier', 'invoice_number', 'date']
    readonly_fields = ['invoice_lines']


@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'line_id', 'name']
    readonly_fields = ['invoice']

    def invoice_number(self, obj: InvoiceLine):
        return obj.invoice_number()
    invoice_number.short_description = 'Fakturanummer'


@admin.register(SerialNumber)
class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ['line', 'serial']
    list_filter = ['line__invoice__supplier']
    readonly_fields = ['line', 'serial']


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'file']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = list_display


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = list_display
