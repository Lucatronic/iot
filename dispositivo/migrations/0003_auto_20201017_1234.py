# Generated by Django 3.1.2 on 2020-10-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0002_publicacioncontrolador'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacionactuador',
            name='retain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publicacioncontrolador',
            name='retain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publicacionsensor',
            name='retain',
            field=models.BooleanField(default=False),
        ),
    ]
