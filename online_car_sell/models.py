import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Avg, Max, Min, Sum
from django.core.validators import MinValueValidator, MaxValueValidator

from online_car_sell.constant import (VehicleAvailablity, YEAR_CHOICES,
                                      VehicleConditionChoices,
                                      VehicleAvailablity)


# Create your models here.
class RegisterVehicle(models.Model):
    """ General/Basic details of the vehicle."""
    car_title = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=120, blank=False)
    mobile_no = models.CharField(_('mobile'), max_length=15, blank=False)
    images = models.ImageField(upload_to='static/image/%Y/%m/%d/',)
    images_1 = models.ImageField(
                null=True, blank=True, upload_to='static/image/%Y/%m/%d/')
    images_2 = models.ImageField(
                null=True, blank=True, upload_to='static/image/%Y/%m/%d/')
    images_3 = models.ImageField(
                null=True, blank=True, upload_to='static/image/%Y/%m/%d/')
    images_4 = models.ImageField(
                null=True, blank=True, upload_to='static/image/%Y/%m/%d/')
    make = models.CharField(max_length=50, blank=False, null=False)
    model = models.CharField(max_length=50, null=False)
    registration_number = models.CharField(max_length=20, null=False)
    year = models.IntegerField(choices=YEAR_CHOICES)
    condition = models.CharField(_("Vehicle_Condition"),
                                 choices=VehicleConditionChoices.choices,
                                 max_length=120)
    pub_date = models.DateTimeField(_('Published Date'), auto_now_add=True)
    # updated_date = models.DateTimeField(_('Updated Date'), auto_now=True)

    # Car still available or Sold...
    vehicle_availablity = models.CharField(_("Available/Sold"), max_length=50,
                                           choices=VehicleAvailablity.choices,
                                           default='AVAILABLE')

    # Vehicle Offer or Selling Price
    # Removed Defaulted values --- default=Decimal('1000.0'),
    vehicle_price = models.DecimalField(max_digits=9, decimal_places=2,
                                        validators=[MinValueValidator(1000),
                                                    MaxValueValidator(100000)],
                                        help_text=_("You can start making\
                                            deal with $1000/-."),
                                        error_messages={
                                            'msg': _('Please fill the\
                                                correct amount ')},
                                        )
    platform_commission = models.DecimalField(max_digits=9, decimal_places=2,
                                              help_text="5% Amount will be\
                                                  charged as a commission.",
                                              )
    net_amount = models.DecimalField(max_digits=9, decimal_places=2,
                                     validators=[MinValueValidator(1000),
                                                 MaxValueValidator(100000)],
                                     help_text="Net amount is display after\
                                            diduction of '5%' as commission.",
                                     error_messages={
                                         'msg': 'Please fill the\
                                             correct amount '},)

    class Meta:
        ordering = ['-pub_date']

    # It will eturn make, model & price of te vehicle & shown on admin
    # Intrective panel.
    def __str__(self):
        return f"{self.id}, {self.make }, {self.model} -- Price {self.vehicle_price}"

class ContactUs(models.Model):
    first_name = models.CharField(_('First_Name'), max_length=50)
    last_name = models.CharField(_('Last_Name'), max_length=50)
    username = models.CharField(_('Username'), max_length=30)
    email = models.EmailField(_('Email Address'), max_length=50)
    mobile = models.CharField(_('Mobile_No'), max_length=15)
    address = models.CharField(_('Address'), max_length=120)
    country = models.CharField(_('Country'), max_length=30)
    state = models.CharField(_('State'), max_length=30)
    zip = models.CharField(_('Zip_Code'), max_length=10)
    additional_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}, {self.email}"



