from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

def year_list(start_year = 1990, current_year = date.today().year + 1):
    year = list((x, x) for x in reversed(range(start_year, current_year)))
    return year

def years(start_year = 1990, current_year = date.today().year + 1):
    year = list(x for x in reversed(range(start_year, current_year)))
    return year

vehicle_condition = ['Very_Poor', 'Poor', 'Fair', 'Good', 'Very_Good', 'Excellent']


def commission(price):
    if 1000 <= int(price) <= 100000:
        platform_commission = (5 * int(price))/100
        net_price = int(price) - platform_commission
        return platform_commission, net_price
    else:
        _price = int(price)
        raise ValidationError(
            _("%(_price)s must be in between 1000 & 100000"),
            params={"price": _price},
        )
    

