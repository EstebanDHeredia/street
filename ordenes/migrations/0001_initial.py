# Generated by Django 3.2 on 2023-01-01 22:11

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
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=300)),
                ('fecha_contratacion', models.DateField()),
                ('rol', models.CharField(blank=True, choices=[('peluquero', 'Peluquero'), ('recepcionista', 'Recepcionista'), ('colorista', 'Colorista'), ('asistente', 'Asistente')], max_length=255)),
                ('fecha_nac', models.DateField(blank=True)),
                ('contacto_emergencia', models.CharField(blank=True, max_length=200)),
                ('tel_emergencia', models.CharField(blank=True, max_length=20)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
