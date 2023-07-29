# Generated by Django 4.2.3 on 2023-07-29 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_cliente_options_servicio_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='servicio',
            name='dispobible',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], null=True),
        ),
    ]