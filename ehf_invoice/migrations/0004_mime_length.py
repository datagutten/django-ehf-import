# Generated by Django 3.1.8 on 2021-12-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ehf_invoice', '0003_invoice_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='mime',
            field=models.CharField(max_length=100, verbose_name='MIME type'),
        ),
    ]