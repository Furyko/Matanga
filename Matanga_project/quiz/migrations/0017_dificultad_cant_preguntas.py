# Generated by Django 3.1.6 on 2021-08-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20210828_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='dificultad',
            name='cant_preguntas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
