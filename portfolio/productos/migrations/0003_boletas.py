# Generated by Django 4.0.5 on 2022-06-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('descripcion', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]