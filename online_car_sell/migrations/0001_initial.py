# Generated by Django 4.0.4 on 2022-04-12 12:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=120)),
                ('mobile_no', models.CharField(max_length=15, verbose_name='mobile')),
                ('images', models.ImageField(upload_to='static/image/%Y/%m/%d/')),
                ('images_1', models.ImageField(blank=True, null=True, upload_to='static/image/%Y/%m/%d/')),
                ('images_2', models.ImageField(blank=True, null=True, upload_to='static/image/%Y/%m/%d/')),
                ('images_3', models.ImageField(blank=True, null=True, upload_to='static/image/%Y/%m/%d/')),
                ('images_4', models.ImageField(blank=True, null=True, upload_to='static/image/%Y/%m/%d/')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=20)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022)),
                ('condition', models.CharField(choices=[('Very_Poor', 'Very_Poor'), ('Poor', 'Poor'), ('Fair', 'Fair'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], max_length=120, verbose_name='Vehicle_Condition')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Published Date')),
                ('Vehicle_Availablity', models.CharField(choices=[('AVAILABLE', 'Available'), ('SOLD', 'Sold')], default='AVAILABLE', max_length=50, verbose_name='Available/Sold')),
                ('vehicle_price', models.DecimalField(decimal_places=2, error_messages={'msg': 'Please fill the                                                correct amount '}, help_text='You can start making                                            deal with $1000/-.', max_digits=9, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(100000)])),
                ('platform_commission', models.DecimalField(decimal_places=2, help_text='5% Amount will be                                                  charged as a commission.', max_digits=9)),
                ('net_amount', models.DecimalField(decimal_places=2, error_messages={'msg': 'Please fill the                                             correct amount '}, help_text="Net amount is display after                                            diduction of '5%' as commission.", max_digits=9, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(100000)])),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
