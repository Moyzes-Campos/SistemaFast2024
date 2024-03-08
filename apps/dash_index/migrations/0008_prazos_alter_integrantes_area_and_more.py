# Generated by Django 4.2.10 on 2024-02-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_index', '0007_delete_profile_alter_integrantes_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prazos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('sub_titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('entrega', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='integrantes',
            name='area',
            field=models.CharField(choices=[('Aerodinâmica', 'Aerodinâmica'), ('Direção', 'Direção e Suspenção'), ('Eletrica', 'Elétrica'), ('Estrutura', 'Estrutura'), ('Freio e Ergonomia', 'Freio e Ergonomia'), ('Powewtrain', 'Powewtrain'), ('Comercial', 'Comercial'), ('Financeiro', 'Financeiro'), ('Gestão', 'Gestão de Pessoas'), ('Marketing', 'Marketing'), ('Qualidade', 'Qualidade'), ('NA', 'Nenhuma')], max_length=50),
        ),
        migrations.AlterField(
            model_name='objetivosarea',
            name='area',
            field=models.CharField(choices=[('Aerodinâmica', 'Aerodinâmica'), ('Direção', 'Direção e Suspenção'), ('Eletrica', 'Elétrica'), ('Estrutura', 'Estrutura'), ('Freio e Ergonomia', 'Freio e Ergonomia'), ('Powewtrain', 'Powewtrain'), ('Comercial', 'Comercial'), ('Financeiro', 'Financeiro'), ('Gestão', 'Gestão de Pessoas'), ('Marketing', 'Marketing'), ('Qualidade', 'Qualidade'), ('NA', 'Nenhuma')], default='Nenhuma', max_length=50),
        ),
    ]
