# Generated by Django 2.2.2 on 2019-06-19 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=20)),
                ('fecha', models.DateField(auto_now=True)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=30)),
                ('precio_actual', models.IntegerField(default=0)),
                ('pmp', models.IntegerField(default=0, editable=False)),
                ('stock', models.IntegerField(default=0, editable=False)),
                ('margen', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_vencimiento', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compra', to='abastecimiento.Compra')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='abastecimiento.Producto')),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalle de Compras',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ManyToManyField(through='abastecimiento.DetalleCompra', to='abastecimiento.Producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='proveedores', to='abastecimiento.Proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
