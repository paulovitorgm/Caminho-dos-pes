# Generated by Django 5.1.2 on 2024-10-25 19:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0004_alter_pacientesmodel_primeiro_atendimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('servico', models.CharField(choices=[('Avaliacao', 'Avaliação'), ('Assepsia completa', 'Assepsia completa'), ('Assepsia plantar', 'Assepsia plantar ou laminar'), ('Ortese', 'Órtese'), ('Curativo', 'Curativo'), ('Parafina', 'Hidratação com parafina'), ('Unha enc', 'Unha encravada'), ('Corte', 'Corte anatômico'), ('Calo', 'Calo'), ('Laser', 'Laser'), ('Outros', 'Outros')], max_length=30)),
                ('pagamento', models.TextField(choices=[('Pix', 'Pix'), ('Credito', 'Crédito'), ('Debito', 'Débito'), ('Dinheiro', 'Dinheiro')], max_length=20)),
                ('total', models.FloatField()),
                ('observacoes', models.CharField(max_length=250)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientesmodel')),
            ],
            options={
                'verbose_name_plural': 'Vendas',
                'db_table': 'vendas',
            },
        ),
    ]