# Generated by Django 3.2.18 on 2023-10-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0004_alter_allocation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accno', models.CharField(max_length=100)),
                ('cardno', models.BigIntegerField()),
                ('cardholder', models.CharField(max_length=100)),
                ('Cvv', models.IntegerField()),
                ('expirydate', models.CharField(max_length=100)),
                ('Balance', models.FloatField()),
            ],
        ),
    ]
