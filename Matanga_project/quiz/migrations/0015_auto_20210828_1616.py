# Generated by Django 3.1.6 on 2021-08-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20210828_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='id_dificultad',
        ),
        migrations.DeleteModel(
            name='Dificultad',
        ),
    ]
