# Generated by Django 4.2.4 on 2023-08-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creargasto',
            name='TipoGasto',
            field=models.CharField(default='Recibo', max_length=50),
            preserve_default=False,
        ),
    ]
