# Generated by Django 3.1.6 on 2021-08-26 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20210825_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='quiz',
        ),
    ]