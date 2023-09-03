from django.contrib import admin
from online_car_sell.models import RegisterVehicle, ContactUs

# Register your models here.
@admin.register(RegisterVehicle, ContactUs)
class AdminCarSite(admin.ModelAdmin):
    pass