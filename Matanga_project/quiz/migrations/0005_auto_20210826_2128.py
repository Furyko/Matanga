# Generated by Django 3.1.6 on 2021-08-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210826_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('pregunta', models.CharField(blank=True, max_length=200, null=True)),
                ('correcto', models.CharField(blank=True, max_length=200, null=True)),
                ('incorrecto_1', models.CharField(blank=True, max_length=200, null=True)),
                ('incorrecto_2', models.CharField(blank=True, max_length=200, null=True)),
                ('incorrecto_3', models.CharField(blank=True, max_length=200, null=True)),
                ('incorrecto_4', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='correcto',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='incorrecto_1',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='incorrecto_2',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='incorrecto_3',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='incorrecto_4',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='pregunta',
        ),
    ]