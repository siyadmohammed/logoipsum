# Generated by Django 5.0.1 on 2024-01-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book1_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author1',
            name='BOOK_ID',
        ),
        migrations.AlterField(
            model_name='book1',
            name='BOOK_ID',
            field=models.AutoField(default=1000, primary_key=True, serialize=False, unique=True),
        ),
    ]
