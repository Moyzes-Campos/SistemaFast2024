# Generated by Django 4.2.10 on 2024-02-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planejamento', '0011_gantt_chart_inicio_atividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gantt_chart',
            name='data_final',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gantt_chart',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]