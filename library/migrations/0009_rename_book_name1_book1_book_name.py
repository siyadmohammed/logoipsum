# Generated by Django 5.0.1 on 2024-02-01 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_rename_book_name_book1_book_name1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book1',
            old_name='BOOK_NAME1',
            new_name='BOOK_NAME',
        ),
    ]