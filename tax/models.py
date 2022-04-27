from dis import dis
from django.db import models
import datetime
from accounts.models import User
from tax.data_extract import final_data
from django.contrib.auth import get_user_model

UserModel = get_user_model()



# Create your models here.
# Get year choices from 2070 to present

def year_choices():
    return [(r,r) for r in range(2070, datetime.date.today().year+58)]


def current_year():
    return datetime.date.today().year + 57



class TaxReceipt(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    province = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    local = models.CharField(max_length=100, blank=True, null=True)
    employee_nature = models.CharField('Nature of Employee', max_length=100, blank=False, null=False)

    fiscal_year = models.CharField(('year'), max_length=100, blank=False, null=False)


    monthly_salary = models.DecimalField('Monthly Salary', max_digits=12, decimal_places=2, blank=False, null=False)

    employee_provident_fund = models.DecimalField('Employee Provident Fund', max_digits=12, decimal_places=2, blank=False, null=False)

    months = models.IntegerField('Months', blank=False, null=False)

    citizen_investment_trust = models.DecimalField('Citizen Investment Trust', max_digits=12, decimal_places=2, blank=False, null=False)

    bonus = models.DecimalField('Bonus', max_digits=12, decimal_places=2, blank=False, null=False)

    insurance = models.DecimalField('Insurance', max_digits=12, decimal_places=2, blank=False, null=False)

    final_tax = models.DecimalField('Final Tax', max_digits=12, decimal_places=2, blank=False, null=False)

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.user.first_name + ' > ' + str(self.final_tax)








