# Generated by Django 2.2.7 on 2020-04-16 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20200416_0344'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
