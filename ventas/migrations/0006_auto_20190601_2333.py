# Generated by Django 2.2 on 2019-06-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20190601_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='monto_final',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]