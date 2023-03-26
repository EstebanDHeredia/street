# Generated by Django 3.2 on 2023-03-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnero', '0003_auto_20230321_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='horario',
        ),
        migrations.AddField(
            model_name='turno',
            name='horario_fin',
            field=models.IntegerField(blank=True, choices=[(0, '09:00'), (1, '09:30'), (2, '10:00'), (3, '10:30'), (4, '11:00'), (5, '11:30'), (6, '12:00'), (7, '12:30'), (8, '13:00'), (9, '13:30'), (10, '14:00'), (11, '14:30'), (12, '15:00'), (13, '15:30'), (14, '16:00'), (15, '16:30'), (16, '17:00'), (17, '17:30'), (18, '18:00'), (19, '18:30'), (20, '19:00'), (21, '19:30'), (22, '20:00')], null=True),
        ),
        migrations.AddField(
            model_name='turno',
            name='horario_inicio',
            field=models.IntegerField(choices=[(0, '09:00'), (1, '09:30'), (2, '10:00'), (3, '10:30'), (4, '11:00'), (5, '11:30'), (6, '12:00'), (7, '12:30'), (8, '13:00'), (9, '13:30'), (10, '14:00'), (11, '14:30'), (12, '15:00'), (13, '15:30'), (14, '16:00'), (15, '16:30'), (16, '17:00'), (17, '17:30'), (18, '18:00'), (19, '18:30'), (20, '19:00'), (21, '19:30'), (22, '20:00')], default=1),
            preserve_default=False,
        ),
    ]
