# Generated by Django 3.1 on 2021-09-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0027_delete_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='preguntas_restantes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
