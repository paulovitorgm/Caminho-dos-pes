# Generated by Django 5.1.2 on 2024-10-25 19:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_alter_pacientesmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientesmodel',
            name='primeiro_atendimento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
