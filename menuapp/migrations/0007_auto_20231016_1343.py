# Generated by Django 3.2.18 on 2023-10-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0006_alter_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='neutral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='positive',
            field=models.IntegerField(default=0),
        ),
    ]