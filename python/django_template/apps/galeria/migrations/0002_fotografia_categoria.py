# Generated by Django 4.2.5 on 2023-10-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NB', 'Nebulosa'), ('ES', 'Estrela'), ('GA', 'Galáxia'), ('PL', 'Planeta')], default='', max_length=2),
        ),
    ]
