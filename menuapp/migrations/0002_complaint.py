# Generated by Django 3.2.18 on 2023-09-22 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('complaints', models.CharField(max_length=300)),
                ('reply', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=50)),
                ('CUSTOMER', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='menuapp.customer')),
            ],
        ),
    ]
