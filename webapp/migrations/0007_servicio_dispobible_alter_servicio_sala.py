# Generated by Django 4.2.3 on 2023-07-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='dispobible',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='sala',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
