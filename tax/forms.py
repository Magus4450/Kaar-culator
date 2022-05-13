from cProfile import label
from django import forms
from .models import TaxReceipt
import datetime

EMPLOYEE_NATURE = [('Unmarried', 'Unmarried'), ('Married', 'Married')]
YEAR_CHOICES = [(str(r-1)+"/"+str(r), str(r-1)+"/"+str(r))
                for r in range(2070, datetime.date.today().year+58)]


class TaxForm(forms.Form):



    employee_nature = forms.CharField(max_length=100, label='Nature of Employee', widget=forms.Select(
        attrs={'class': 'form-control'}, choices=EMPLOYEE_NATURE))

    # Show fiscal year in the frontend
    fiscal_year = forms.CharField(max_length=100, label='Fiscal Year', widget=forms.Select(
        attrs={'class': 'form-control'}, choices=YEAR_CHOICES))

    # Show province in frontend

    monthly_salary = forms.DecimalField(
        max_digits=12, decimal_places=2, label='Monthly Salary', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    employee_provident_fund = forms.DecimalField(
        max_digits=12, decimal_places=2, label='Employee Provident Fund', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    months = forms.IntegerField(
        label='Months', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    citizen_investment_trust = forms.DecimalField(
        max_digits=12, decimal_places=2, label='Citizen Investment Trust', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    bonus = forms.DecimalField(max_digits=12, decimal_places=2, label='Bonus',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))

    insurance = forms.DecimalField(max_digits=12, decimal_places=2, label='Insurance',
                                   widget=forms.NumberInput(attrs={'class': 'form-control'}))

    


class TaxForm2(forms.ModelForm):

    class Meta:
        model = TaxReceipt

        fields = [
            'province',
            'district',
            'local',
            'employee_nature',
            'fiscal_year',
            'monthly_salary',
            'employee_provident_fund',
            'months',
            'citizen_investment_trust',
            'bonus',
            'insurance',

          ]
