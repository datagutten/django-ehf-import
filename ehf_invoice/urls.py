from django.urls import path

from ehf_invoice import views

app_name = 'ehf_invoice'
urlpatterns = [
    path('', views.index, name='index'),
    path('suppliers', views.suppliers, name='suppliers'),
    path('supplier', views.suppliers),
    path('supplier/<str:supplier>', views.show_supplier, name='supplier'),
    path('invoice', views.show_invoice, name='invoice'),
    path(
        'invoice/<str:invoice_number>', views.show_invoice, name='show_invoice'
    ),
    path(
        'serial',
        views.find_serial,
        name='find_serial_number_get',
    ),
    path(
        'serial/<str:serial_number>',
        views.find_serial,
        name='find_serial_number',
    ),
]
