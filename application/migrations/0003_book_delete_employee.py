# Generated by Django 5.0.3 on 2024-05-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_employee_aadhar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booknumber', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
