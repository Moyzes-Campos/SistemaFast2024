# Generated by Django 4.2.10 on 2024-02-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_index', '0006_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='integrantes',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='integrantes'),
        ),
    ]
