# Generated by Django 4.2.4 on 2023-08-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_creargasto_tipogasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creargasto',
            name='TipoGasto',
            field=models.CharField(choices=[('recibo', 'Recibo'), ('deuda', 'Deuda'), ('comida', 'Comida'), ('otros', 'Otros')], max_length=50),
        ),
    ]