# Generated by Django 3.1.6 on 2021-08-28 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_quiz'),
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
