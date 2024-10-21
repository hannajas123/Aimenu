# Generated by Django 3.2.18 on 2023-09-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=20)),
                ('amount', models.CharField(max_length=30)),
                ('CUSTOMER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_no', models.CharField(max_length=30)),
                ('no_of_seats', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Special_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MENU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=20)),
                ('time', models.TimeField(max_length=20)),
                ('review', models.CharField(max_length=30)),
                ('rating', models.CharField(max_length=30)),
                ('CUSTOMER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.customer')),
                ('MENU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.CharField(max_length=40)),
                ('date', models.DateField(max_length=30)),
                ('ORDERMAIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.order_main')),
            ],
        ),
        migrations.CreateModel(
            name='Order_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=30)),
                ('MENU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.menu')),
                ('ORDERMAIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.order_main')),
            ],
        ),
        migrations.CreateModel(
            name='Order_delay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time_in_minutes', models.TimeField(max_length=20)),
                ('ORDERMAIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.order_main')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.login'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=30)),
                ('CUSTOMER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.customer')),
                ('MENU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('date', models.DateField(max_length=30)),
                ('time', models.TimeField(max_length=30)),
                ('ORDERMAIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.order_main')),
                ('STAFF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuapp.staff')),
            ],
        ),
    ]
