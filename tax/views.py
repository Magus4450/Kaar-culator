from cgitb import text
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import TaxReceipt
from .forms import TaxForm, TaxForm2
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa




def tax_pdf(request, pk):


    tax = TaxReceipt.objects.get(pk=pk)
    template = get_template('templates/tax/tax_pdf.html')
    user = request.user
    context = {'tax': tax, 'user':user}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tax_receipt.pdf"'

    
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    



class TaxDetailView(DetailView):
    context_object_name = 'tax'
    model = TaxReceipt
    template_name = 'templates/tax/tax_details.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(TaxDetailView, self).dispatch(request, *args, **kwargs)


@login_required(login_url=reverse_lazy('accounts:login'))
def tax_view(request):

    if request.method == "POST":
        form = TaxForm2(request.POST)
        print(request.POST)
        print("BEFORE VALID")
        if form.is_valid():
            print(form.cleaned_data)

            sum_epf_cit = form.cleaned_data["employee_provident_fund"] + form.cleaned_data["citizen_investment_trust"]
            insurance = form.cleaned_data["insurance"]

            total_income = (form.cleaned_data["monthly_salary"]*form.cleaned_data["months"]) + form.cleaned_data["bonus"]
            total_deduction = sum_epf_cit + insurance

            net_assessable = total_income - total_deduction
            print("TOTAL NET ACCESSABLE", net_assessable)
            

            if form.cleaned_data["employee_nature"] == "Unmarried":
                bal = float(net_assessable)
                tax = 0
                if net_assessable > 0:
                    tax += min(400000,bal) * 0.01
                    print(">", min(400000,bal),": 1% :", tax)
                    bal = bal - 400000

                
                if net_assessable > (400000):
                    tax += min(bal,100000) *0.1
                    print(">", min(bal,100000),": 10% :", tax)
                    bal = bal - 100000
                    

                if net_assessable > (400000+100000):
                    tax += min(bal,200000) *0.2
                    print(">", min(bal,200000),": 20% :", tax)
                    bal = bal - 200000

                if net_assessable > (400000+100000+200000):
                    tax += min(bal,1300000) *0.3
                    print(">", min(bal,1300000),": 30% :", tax)
                    bal = bal - 1300000
                
                if net_assessable > (400000+100000+200000+1300000):
                    tax += bal * 0.36
                    print(">", bal,": 36% :", tax)




            else:
                bal = float(net_assessable)
                tax = 0
                if net_assessable > 0:
                    tax += min(450000,bal) * 0.01
                    print(">", min(450000,bal),": 1% :", tax)
                    bal = bal - 450000

                
                if net_assessable > (450000):
                    tax += min(bal,100000) *0.1
                    print(">", min(bal,100000),": 10% :", tax)
                    bal = bal - 100000
                    

                if net_assessable > (450000+100000):
                    tax += min(bal,200000) *0.2
                    print(">", min(bal,200000),": 20% :", tax)
                    bal = bal - 200000

                if net_assessable > (450000+100000+200000):
                    tax += min(bal,1250000) *0.3
                    print(">", min(bal,1250000),": 30% :", tax)
                    bal = bal - 1250000
                
                if net_assessable > (450000+100000+200000+1250000):
                    tax += bal * 0.36
                    print(">", bal,": 36% :", tax)

        
            tax_data = TaxReceipt.objects.create(
                user = request.user,
                province = form.cleaned_data["province"],
                district = form.cleaned_data["district"],
                local = form.cleaned_data["local"],
                employee_nature = form.cleaned_data["employee_nature"],
                fiscal_year = form.cleaned_data["fiscal_year"],
                monthly_salary = form.cleaned_data["monthly_salary"],
                employee_provident_fund = form.cleaned_data["employee_provident_fund"],
                citizen_investment_trust = form.cleaned_data["citizen_investment_trust"],
                insurance = form.cleaned_data["insurance"],
                months = form.cleaned_data["months"],
                bonus = form.cleaned_data["bonus"],
                final_tax = tax,
            )
            tax_data.save()
            return redirect('tax:detail', pk=tax_data.pk)
        else:
            print("INVALID")
        # form = TaxForm.objects.create(**form)
        
        form = TaxForm(request.POST)    
        
    elif request.method == "GET":
        form = TaxForm(initial={'fiscal_year': '2078/2079'})
        print(form.as_p)

    return render(request, 'templates/tax/tax.html', {"form": form})

