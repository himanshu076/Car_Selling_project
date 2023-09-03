import datetime

YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))

print(YEAR_CHOICES)