# Generated by Django 4.2.5 on 2023-10-04 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0008_fotografia_usuario_alter_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 16, 11, 38, 22574)),
        ),
    ]
