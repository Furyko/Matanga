# Generated by Django 3.1.6 on 2021-08-27 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20210826_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='categoria_preg',
        ),
    ]