# Generated by Django 4.0.10 on 2023-10-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='descripcion',
            field=models.IntegerField(null=True, verbose_name='Cantidad'),
        ),
    ]
