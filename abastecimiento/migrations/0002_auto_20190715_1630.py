# Generated by Django 2.2.2 on 2019-07-15 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abastecimiento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='pmp',
            new_name='ppp',
        ),
    ]
