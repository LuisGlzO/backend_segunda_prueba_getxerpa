# Generated by Django 4.2.4 on 2023-08-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_remove_categoria_id_presupuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]