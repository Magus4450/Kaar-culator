from django.test import TestCase
import datetime
# Create your tests here.
def year_choices():
    return [(str(r-1)+"/"+str(r),str(r-1)+"/"+str(r)) for r in range(2070, datetime.date.today().year+58)]

print(year_choices())