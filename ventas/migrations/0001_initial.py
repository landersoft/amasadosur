# Generated by Django 2.2 on 2019-04-19 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abastecimiento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalleventa', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_venta', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abastecimiento.Producto')),
            ],
            options={
                'verbose_name': 'Detalle de Ventas',
                'ordering': ['id_venta'],
                'verbose_name_plural': 'Detalle de Ventas',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('producto', models.ManyToManyField(through='ventas.DetalleVenta', to='abastecimiento.Producto')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pago', models.CharField(blank=True, max_length=100, null=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Cliente')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta'),
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pago', models.CharField(blank=True, max_length=100, null=True)),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
            ],
        ),
    ]