# Generated by Django 5.1.2 on 2024-11-01 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
