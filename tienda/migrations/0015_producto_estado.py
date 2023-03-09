# Generated by Django 3.2 on 2023-03-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0014_auto_20230308_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('en_venta', 'en_venta'), ('pausado', 'pausado'), ('eliminado', 'Eliminado')], default='en_venta', max_length=255),
        ),
    ]
