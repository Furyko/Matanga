# Generated by Django 3.1.6 on 2021-08-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_resultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('cel', models.ImageField(null=True, upload_to='')),
                ('clave', models.CharField(max_length=100)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='cantidad_de_preguntas',
            field=models.IntegerField(),
        ),
    ]
