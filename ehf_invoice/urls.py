from django.urls import path

from ehf_invoice import views

app_name = 'ehf_invoice'
urlpatterns = [
    path('supplier/<str:supplier>', views.show_supplier, name='supplier'),
    path('invoice', views.show_invoice, name='invoice'),
    path(
        'invoice/<str:invoice_number>', views.show_invoice, name='show_invoice'
    ),
    path(
        'serial/<str:serial_number>',
        views.find_serial,
        name='find_serial_number',
    ),
]
