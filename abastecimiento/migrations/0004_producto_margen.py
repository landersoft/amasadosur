# Generated by Django 2.2 on 2019-05-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimiento', '0003_auto_20190524_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='margen',
            field=models.IntegerField(default=20),
        ),
    ]
