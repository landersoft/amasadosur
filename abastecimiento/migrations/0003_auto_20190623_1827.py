# Generated by Django 2.2.2 on 2019-06-23 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimiento', '0002_auto_20190623_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio_actual',
            new_name='precio_venta_unitario',
        ),
    ]
