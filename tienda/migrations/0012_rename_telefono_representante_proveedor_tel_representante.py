# Generated by Django 3.2 on 2022-12-31 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_rename_nombre_compañia_proveedor_nombre_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='telefono_representante',
            new_name='tel_representante',
        ),
    ]
