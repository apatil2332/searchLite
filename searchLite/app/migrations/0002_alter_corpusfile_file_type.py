# Generated by Django 5.0.4 on 2024-05-01 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpusfile',
            name='file_type',
            field=models.CharField(max_length=100),
        ),
    ]
