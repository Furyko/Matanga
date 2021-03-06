# Generated by Django 3.1.6 on 2021-09-03 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0025_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='fecha',
        ),
        migrations.AddField(
            model_name='partida',
            name='id_fecha',
            field=models.ForeignKey(blank=True, db_column='id_fecha', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.fecha'),
        ),
    ]
