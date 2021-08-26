# Generated by Django 3.1.6 on 2021-08-26 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_pregunta_id_respuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.CharField(max_length=50)),
                ('topico', models.CharField(max_length=200)),
                ('id_pregunta', models.ForeignKey(blank=True, db_column='id_pregunta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.pregunta')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cel',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Resultado',
        ),
    ]