# Generated by Django 4.2.10 on 2024-02-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planejamento', '0008_atividade_gantt_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gantt_chart',
            name='percent_complete',
            field=models.IntegerField(default=0),
        ),
    ]