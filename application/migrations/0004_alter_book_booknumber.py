# Generated by Django 5.0.3 on 2024-05-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_book_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='booknumber',
            field=models.IntegerField(unique=True),
        ),
    ]
