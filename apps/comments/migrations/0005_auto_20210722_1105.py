# Generated by Django 2.2.6 on 2021-07-22 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20210722_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='movie',
            new_name='hostel',
        ),
    ]
