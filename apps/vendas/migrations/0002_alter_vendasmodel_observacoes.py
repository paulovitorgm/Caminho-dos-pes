# Generated by Django 5.1.2 on 2024-11-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendasmodel',
            name='observacoes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
