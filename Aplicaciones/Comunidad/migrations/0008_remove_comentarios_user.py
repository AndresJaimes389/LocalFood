# Generated by Django 4.0.10 on 2023-11-24 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comunidad', '0007_alter_comentarios_table_alter_respuesta_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='user',
        ),
    ]