# Generated by Django 2.2.6 on 2021-07-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_auto_20210720_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.PositiveIntegerField(default=100, verbose_name='Цена за сутки:'),
        ),
    ]
