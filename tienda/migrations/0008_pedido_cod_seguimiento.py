# Generated by Django 3.2 on 2022-12-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_rename_total_pedido_monto_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cod_seguimiento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
