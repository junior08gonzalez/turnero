# Generated by Django 4.2.3 on 2023-07-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='prioridad',
            field=models.CharField(blank=True, null=True),
        ),
    ]
