# Generated by Django 3.2.18 on 2023-10-06 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0005_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
