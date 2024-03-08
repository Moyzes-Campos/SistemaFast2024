# Generated by Django 4.2.10 on 2024-02-29 11:38

from django.db import migrations
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_index', '0003_integrantes_foto_alter_integrantes_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='foto',
            field=pictures.models.PictureField(aspect_ratios=['1/1'], blank=True, breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, null=True, pixel_densities=[1, 2], upload_to='Integrantes'),
        ),
    ]
