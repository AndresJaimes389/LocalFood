# Generated by Django 4.0.10 on 2023-10-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_receta', models.CharField(max_length=255)),
                ('Descripcion', models.TextField()),
                ('Ingredientes', models.TextField()),
                ('Ingrediente_principal', models.CharField(max_length=255)),
            ],
        ),
    ]