# Generated by Django 2.2.6 on 2021-07-25 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210725_0854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-create_at',)},
        ),
    ]