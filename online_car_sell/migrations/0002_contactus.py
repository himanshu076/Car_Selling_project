# Generated by Django 4.0.4 on 2022-04-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_car_sell', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First_Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last_Name')),
                ('username', models.CharField(max_length=30, verbose_name='Username')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobile_No')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('state', models.CharField(max_length=30, verbose_name='State')),
                ('zip', models.CharField(max_length=10, verbose_name='Zip_Code')),
            ],
        ),
    ]