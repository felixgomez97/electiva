# Generated by Django 2.2.4 on 2019-11-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-created'], 'verbose_name': 'noticia', 'verbose_name_plural': 'noticias'},
        ),
    ]