# Generated by Django 3.2 on 2023-03-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_mensaje_asunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resumen',
            field=models.CharField(default='Texto Resumen del post', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
