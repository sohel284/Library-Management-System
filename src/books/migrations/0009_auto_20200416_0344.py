# Generated by Django 2.2.7 on 2020-04-16 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200414_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_id',
        ),
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn ">ISBN number</a>', max_length=13, primary_key=True, serialize=False, verbose_name='ISBN'),
        ),
    ]
