# Generated by Django 3.1.1 on 2020-10-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='correct',
            field=models.BooleanField(blank=True, default=False, verbose_name='Correta?'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True, verbose_name='Identificador'),
        ),
    ]
