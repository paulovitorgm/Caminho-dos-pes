# Generated by Django 5.1.2 on 2024-10-25 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0004_alter_anamnesemodel_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesemodel',
            name='data',
            field=models.DateField(default=datetime.date(2024, 10, 24)),
        ),
    ]
