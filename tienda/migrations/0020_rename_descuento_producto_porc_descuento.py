# Generated by Django 3.2 on 2023-03-09 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0019_alter_producto_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='descuento',
            new_name='porc_descuento',
        ),
    ]