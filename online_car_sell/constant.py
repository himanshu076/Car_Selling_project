import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils import year_list


# YEAR_CHOICES = [(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003),
#                 (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007),
#                 (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011),
#                 (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015),
#                 (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019),
#                 (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)
#                 ]

YEAR_CHOICES = year_list()


class YearChoice(models.TextChoices):
    VERY_POOR = 'Very_Poor', _('Very_Poor')
    POOR = 'Poor', _('Poor')
    Fair = 'Fair', _('Fair')
    Good = 'Good', _('Good')
    Very_Good = 'Very Good', _('Very Good')
    Excellent = 'Excellent', _('Excellent')


class VehicleConditionChoices(models.TextChoices):
    VERY_POOR = 'Very_Poor', _('Very_Poor')
    POOR = 'Poor', _('Poor')
    Fair = 'Fair', _('Fair')
    Good = 'Good', _('Good')
    Very_Good = 'Very Good', _('Very Good')
    Excellent = 'Excellent', _('Excellent')

class VehicleAvailablity(models.TextChoices):
    AVAILABLE = 'AVAILABLE', _('Available')
    SOLD = 'SOLD', _('Sold')



# • Very Poor
# • Poor
# • Below Average
# • Fair
# • Average
# • Good
# • Very Good
# • Above Average
# • Excellent