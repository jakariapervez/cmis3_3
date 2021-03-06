from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from .models import Dpp_allocation,Budget_allocation,FinancialYear
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
"""
#dpp allocation................................................................................
...........................................................................................
"""
def index(request):
    #now=datetime.datetime.now()
    #html="<html><body> It is now %s </body></html>"%now
    #context={}
    #return render(request,'pac/add_edit_drop_progress_item.html', context)
    #haors = Haor.objects.all()
    dppitems = Dpp_allocation.objects.all()
    return render(request, 'pac/edit_dpp_intervention2.html', {'dppitems': dppitems})
from .forms import DPP_intervention_form,ProgressQuantityForm
from django.template.loader import render_to_string
@login_required
def save_ivt_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            dppitems = Dpp_allocation.objects.all()
            data['html_ivt_list'] = render_to_string('pac/includes/partial_ivt_list.html', {
                'dppitems': dppitems
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)







@login_required
def create_DPP_Allocation(request):
    if request.method == 'POST':
        form = DPP_intervention_form(request.POST)
    else:
        form = DPP_intervention_form()
    return save_ivt_form(request, form, 'pac/includes/partial_ivt_create.html')

@login_required
def update_DPP_Allocation(request, pk):
    ivt = get_object_or_404(Dpp_allocation, pk=pk)
    print(ivt)

    if request.method == 'POST':
        form = DPP_intervention_form(request.POST, instance=ivt)
    else:
        form = DPP_intervention_form(instance=ivt)
    return save_ivt_form(request, form, 'pac/includes/partial_ivt_update.html')

@login_required
def delete_DPP_Allocation2(request, pk):
    ivt = get_object_or_404(Dpp_allocation, pk=pk)
    print(ivt)
    data = dict()
    if request.method == 'POST':

        ivt.delete()
        data['form_is_valid'] = True
        dppitems = Dpp_allocation.objects.all()
        data['html_ivt_list'] = render_to_string('pac/includes/partial_ivt_list.html', {
            'dppitems': dppitems
        })
    else:
        context = {'ivt': ivt}
        data['html_form'] = render_to_string('pac/includes/partial_ivt_delete.html', context, request=request)
    return JsonResponse(data)

@login_required
def delete_DPP_Allocation(request, pk):
    ivt = get_object_or_404(Dpp_allocation, pk=pk)
    data = dict()
    if request.method == 'POST':
        ivt.delete()
        data['form_is_valid'] = True
        dppitems = Dpp_allocation.objects.all()
        data['html_ivt_list'] = render_to_string('pac/includes/partial_ivt_list.html', {
            'dppitems': dppitems
        })
        print(data['html_ivt_list'])
    else:
        context = {'ivt': ivt}
        data['html_form'] = render_to_string('pac/includes/partial_ivt_delete.html', context, request=request)
    return JsonResponse(data)
@login_required
def add_budget_item(request):
    Dppitems=  Budget_allocation.objects.all()
    #contracts = Contract.objects.all()
    #civts = Contract.objects.all()
    context = {'Dppitems': Dppitems,}
    return render(request, 'pac/add_edit_drop_progress_item.html', context)

"""
#Budget allocation
"""
@login_required
def input_budget_allocation(request):

    # contracts = Contract.objects.all()
    # civts = Contract.objects.all()
    dppitems = Budget_allocation.objects.all()
    fyears=FinancialYear.objects.all()
    return render(request, 'pac/budget_allocation.html', {'dppitems': dppitems,'fyears':fyears})

"""   
budget allocation .Budget allocation budget allocation .Budget allocation budget allocation .Budget allocation 
budget allocation .Budget allocation budget allocation .Budget allocation budget allocation .Budget allocation 
budget allocation .Budget allocation budget allocation .Budget allocation budget allocation .Budget allocation 
budget allocation .Budget allocation budget allocation .Budget allocation budget allocation .Budget allocation 
"""
@login_required
def save_budget_form(request, fy,form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            dppitems = Budget_allocation.objects.all().filter(Financial_year=fy)
            data['html_ivt_list'] = render_to_string('pac/includes/budget_allocation/partial_budget_allocation_list2.html', {
                'dppitems': dppitems
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

from .forms import Budget_allocation_form
@login_required
def update_Budget_Allocation(request, pk):
    ivt = get_object_or_404(Budget_allocation, pk=pk)
    fy=ivt.Financial_year
    print(ivt)

    if request.method == 'POST':
        form = Budget_allocation_form(request.POST, instance=ivt)
    else:
        form = Budget_allocation_form(instance=ivt)

    return save_budget_form(request, fy,form, 'pac/includes/budget_allocation/partial_ivt_update.html')

@login_required
def delete_Budget_Allocation2(request, pk):
    ivt = get_object_or_404(Dpp_allocation, pk=pk)
    print(ivt)
    data = dict()
    if request.method == 'POST':

        ivt.delete()
        data['form_is_valid'] = True
        dppitems = Dpp_allocation.objects.all()
        data['html_ivt_list'] = render_to_string('pac/includes/partial_ivt_list.html', {
            'dppitems': dppitems
        })
    else:
        context = {'ivt': ivt}
        data['html_form'] = render_to_string('pac/includes/partial_ivt_delete.html', context, request=request)
    return JsonResponse(data)

def list_budget_item_sort_by_fy(request, pk):
    print(pk)
    dppitems = Budget_allocation.objects.all().filter(Financial_year=pk)

    data = dict()
    data['html_ivt_list'] = render_to_string('pac/includes/budget_allocation/partial_budget_allocation_list2.html', {
        'dppitems': dppitems
    })

    return JsonResponse(data)

"""  Invoice Image and Invoice  """
from .forms import InvoiceImageForm
from .models import InvoiceImage
@login_required
def Invoice_image_upload(request):
    if request.method == 'POST':
        form =InvoiceImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = InvoiceImage()
            image.invoice_image= form.cleaned_data['invoice_image']
            image.issuing_date = form.cleaned_data['issuing_date']
            image.uploaded_date = form.cleaned_data['uploaded_date']
            image.description=form.cleaned_data['description']
            image.save()
            return redirect('pac_index')
    else:
        form = InvoiceImageForm()
    return render(request, 'pac/includes/construction_image/construction_image_upload_form.html', {
        'form': form
    })
""" Invoice Related views"""
from .models import Invoice_details
@login_required
def invoice_list(request):

    # contracts = Contract.objects.all()
    # civts = Contract.objects.all()
<<<<<<< HEAD
<<<<<<< HEAD
    invoices = Invoice_details.objects.all()
    fyears=FinancialYear.objects.all()
    return render(request, 'pac/invoice_list.html', {'invoices': invoices,'fyears':fyears})
=======
=======
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
    invoices = Invoice_details.objects.all().order_by('-date')
    fyears=FinancialYear.objects.all()
    months = ["ALL", 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
    return render(request, 'pac/invoice_list.html', {'invoices': invoices,'fyears':fyears,'months':months})
<<<<<<< HEAD
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
=======
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
@login_required
def list_invoices_sort_by_fy(request,pk):
    myyear = FinancialYear.objects.get(pk=pk)
    fyears = FinancialYear.objects.all()
    data=dict()
    invoices = Invoice_details.objects.filter(FinancialYear=myyear)
    data['html_ivt_list']=render_to_string('pac/includes/invoices/partial_invoices_list.html', {
        'invoices': invoices
    })

    return  JsonResponse(data)

<<<<<<< HEAD
<<<<<<< HEAD

=======
=======
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
def invoice_list_sort_by_all(request):
    data=dict()
    year_id=request.GET['fy']
    month=request.GET['month']
    #ecode=request.GET['ecode']
    fy=FinancialYear.objects.get(pk=year_id)
    invoices=Invoice_details.objects.filter( FinancialYear=fy).order_by('-date').order_by('-Invoice_no')
    if month !="ALL":
        invoices=invoices.filter(Month=month)

    print("FY={} month={}".format(year_id,month))
    #dppitems = Expenditure_details.objects.all()
    data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
        'invoices': invoices
    })
    return JsonResponse(data)
<<<<<<< HEAD
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
=======
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651





from .models import Invoice_details
from .auxilaryquery import financialYearFromDate
@login_required
def save_invoice_form(request,form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            #form.save()
            invoice=Invoice_details()
            invoice.date=form.cleaned_data['date']
            invoice.Invoice_no=form.cleaned_data['Invoice_no']
            invoice.BatchType=form.cleaned_data['BatchType']
            invoice.Description=form.cleaned_data['Description']
            invoice.Total_amount=0.0
            invoice.document_id=form.cleaned_data['document_id']
            invoice.FinancialYear=financialYearFromDate(invoice.date)
            invoice.Month=invoice.date.month
            #'Invoice_no', 'date', 'BatchType', 'Description', 'Total_amount', 'document_id',
            invoice.save()





            data['form_is_valid'] = True
            invoices = Invoice_details.objects.all()
            data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def save_invoice_form2(request,form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            invoices = Invoice_details.objects.all()
            data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


from .auxilaryquery import financialYearFromDate
from .forms import Invoice_details_Forms
@login_required
def Edit_invoice(request,pk):
    ivt = get_object_or_404(Invoice_details, pk=pk)
    war_start =datetime.datetime.now()
    mydate=datetime.datetime.date(war_start)

    fy=financialYearFromDate(mydate)
    print("fy={}".format(fy))
    if request.method == 'POST':
        form = Invoice_details_Forms(request.POST, instance=ivt)
    else:
        form = Invoice_details_Forms(instance=ivt)
    return save_invoice_form2(request, form, 'pac/includes/invoices/partial_ivt_update.html')
@login_required
def Add_invoice(request):
    if request.method == 'POST':
        form = Invoice_details_Forms(request.POST)
    else:
        form = Invoice_details_Forms()
    return save_invoice_form(request, form, 'pac/includes/invoices/partial_ivt_create.html')


@login_required
def Delete_invoice(request, pk):
    ivt = get_object_or_404(Invoice_details, pk=pk)
    data = dict()
    if request.method == 'POST':
        ivt.delete()
        data['form_is_valid'] = True
        invoices = Invoice_details.objects.all()
        data['html_ivt_list'] =render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices
            })
    else:
        context = {'ivt': ivt}
        data['html_form'] = render_to_string('pac/includes/invoices/partial_ivt_delete.html', context, request=request)
    return JsonResponse(data)


"""" View Function for Expenditure details   """
from .models import Expenditure_details
from .forms import Expenditure_details_Forms
@login_required
def save_expenditure_form(request,form,invoice, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            #form.save()
            #invoice.save()
            data['form_is_valid'] = True
            invoices = Invoice_details.objects.all()
            data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,'invoice':invoice}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
def save_expenditure_form2(request,form,invoice, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            #form.save()
            #invoice.save()
            data['form_is_valid'] = True
            """ 
            invoices = Invoice_details.objects.all()
            data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices
            })
             """
            invoices = Expenditure_details.objects.all()
            data['html_ivt_list'] = render_to_string('pac/includes/expenditures/partial_expenditures_list.html', {
                'invoices': invoices
            })



        else:
            data['form_is_valid'] = False
        context = {'form': form,'invoice':invoice}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

"""     
def Add_Expenditure(request,pk):
    invoice= get_object_or_404(Invoice_details, pk=pk)
    expenditure=Expenditure_details()
    if request.method=='POST':
        form=Expenditure_details_Forms(request.POST)
        if form.is_valid():
            gob=form.cleaned_data['Gob']
            rpa=form.cleaned_data['Rpa']
            dpa=form.cleaned_data['Dpa']
            total=gob+dpa+rpa
            print("GoB={} DPA={} RPA={} Total={}".format(gob,dpa,rpa,total))
            #form.fields['Total']=total
            #form.cleaned_data['Total']=total
            expenditure.Invoice_details = invoice
            expenditure.Gob=gob
            expenditure.Dpa=dpa
            expenditure.Rpa=rpa
            expenditure.Total=total
            expenditure.Budget_allocation=form.cleaned_data['Budget_allocation']
            expenditure.date=invoice.date
            expenditure.save()
            #expenditure
            #form.save()
        return redirect(expenditure_list)
    else:
        form=Expenditure_details_Forms()
        form.fields["Invoice_details"].initial =  invoice
    return save_expenditure_form(request, form,invoice, 'pac/includes/invoices/partial_expenditure_create.html')
"""










from .auxilaryquery import validateExpenditure
@login_required
def Add_Expenditure(request,pk):
    invoice= get_object_or_404(Invoice_details, pk=pk)
    expenditure=Expenditure_details()
    data = dict()
    if request.method=='POST':
        form=Expenditure_details_Forms(request.POST)
        #print(form)
        if form.is_valid():
            myexpenditure=validateExpenditure(form,invoice)
            print("isvalid={} cumTotal={}".format(myexpenditure['validity'],myexpenditure['cumtotal']))
            expenditure=myexpenditure['expenditure']
            cumTotal=myexpenditure['cumtotal']
            if myexpenditure['validity']:
                expenditure.save()
                #Invoice_details.objects.filter(pk=pk).update(Total=cumTotal)
                #Expenditure_details.objects.filter(pk=pk).update(Total=cumTotal)
                invoice.Total_amount=cumTotal
                invoice.save()
                data['form_is_valid'] = True
                #invoice.save()
                invoices = Invoice_details.objects.all()
                data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices })
                #return redirect(expenditure_list)
                #return JsonResponse(data)
            #expenditure.save()
            #expenditure
            #form.save()
        else:
            data['form_is_valid'] = False

    else:
        form=Expenditure_details_Forms()
        #form.fields["Invoice_details"].initial =  invoice
        #form.fields['date'].initial=invoice.date
        context = {'form': form, 'invoice': invoice}
        data['html_form'] = render_to_string('pac/includes/invoices/partial_expenditure_create.html', context, request=request)
    return JsonResponse(data)

    #return save_expenditure_form(request, form,invoice, 'pac/includes/invoices/partial_expenditure_create.html')
@login_required
def Add_Expenditure2(request,pk):
    invoice= get_object_or_404(Invoice_details, pk=pk)
    expenditure=Expenditure_details()
    if request.method=='POST':
        form=Expenditure_details_Forms(request.POST)
        """    
        if form.is_valid():
            data = dict()
            myexpenditure=validateExpenditure(form,invoice)
            print("isvalid={}".format(myexpenditure['validity']))
            expenditure=myexpenditure['expenditure']
            cumTotal=myexpenditure['cumtotal']
            if myexpenditure['validity']:
                expenditure.save()
                invoice.Total=cumTotal
                invoice.save()
                data['form_is_valid'] = True
                invoice.save()
                invoices = Invoice_details.objects.all()
                data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', {
                'invoices': invoices })
                #return redirect(expenditure_list)
                #return JsonResponse(data)
            #expenditure.save()
            #expenditure
            #form.save()
          """
    else:
        form=Expenditure_details_Forms()
        form.fields["Invoice_details"].initial =  invoice
    return save_expenditure_form(request, form,invoice, 'pac/includes/invoices/partial_expenditure_create.html')
@login_required
def UpdateExpenditure2(request,pk):
    ivt = get_object_or_404(Expenditure_details, pk=pk)
    invoices=list(Invoice_details.objects.filter(expenditure_details__pk=pk))
    invoice=invoices[0]
    print(invoice)
    print("invoice no={}".format(invoice.Invoice_no))
    #invoice = get_object_or_404(Invoice_details, pk=ivt.Invoice_details.pk)
    #war_start = datetime.datetime.now()
    if request.method == 'POST':
        form = Expenditure_details_Forms(request.POST)
        if form.is_valid():
            data = dict()
            myexpenditure = validateExpenditure(form,invoice)
            print("isvalid={} cumTotal={}".format(myexpenditure['validity'], myexpenditure['cumtotal']))
            expenditure = myexpenditure['expenditure']
            cumTotal = myexpenditure['cumtotal']
            if myexpenditure['validity']:
                form.save()
                #ivt.Gob=expenditure.Gob
                #ivt.Dpa=expenditure.Dpa
                #ivt.Rpa=expenditure.Rpa
                #ivt.Total=expenditure.Total
                #ivt.save()
                # Invoice_details.objects.filter(pk=pk).update(Total=cumTotal)
                # Expenditure_details.objects.filter(pk=pk).update(Total=cumTotal)
                invoice.Total_amount = cumTotal
                invoice.save()
                data['form_is_valid'] = True
                # invoice.save()
                invoices = Invoice_details.objects.all()
                #data['html_ivt_list'] = render_to_string('pac/includes/invoices/partial_invoices_list.html', { 'invoices': invoices})
                data['html_ivt_list'] = render_to_string('pac/includes/expenditures/partial_expenditures_list.html', {
                    'invoices': invoices
                })
                # return redirect(expenditure_list)
                # return JsonResponse(data)
            # expenditure.save()
            # expenditure
            # form.save()

    else:
        form = Expenditure_details_Forms(instance=ivt)
    return save_expenditure_form2(request, form, invoice, 'pac/includes/expenditures/partial_ivt_update.html')

    """   
    ivt = get_object_or_404(Expenditure_details, pk=pk)
    if request.method == 'POST':
        form = Expenditure_details_Forms(request.POST)
    else:
        form = Invoice_details_Forms()
    return save_invoice_form(request, form, 'pac/includes/invoices/partial_ivt_create.html')
    """
from .forms import Expenditure_details_Edit_Forms
from .auxilaryquery import validateExpenditureEditForm,getInvoiceTotal2
@login_required
def UpdateExpenditure(request, pk):
    ivt = get_object_or_404(Expenditure_details, pk=pk)
    invoices = list(Invoice_details.objects.filter(expenditure_details__pk=pk))
    invoice = invoices[0]
    print(invoices)
    print("invoice no={} date={} Total amount={}".format(invoice.Invoice_no,invoice.date,invoice.Total_amount))

    data = dict()
    if request.method == 'POST':
        form = Expenditure_details_Edit_Forms(request.POST,instance=ivt)
        if form.is_valid():
            data = dict()
            myexpenditure = validateExpenditureEditForm(form,ivt)
            #print("isvalid={}".format(myexpenditure['isValid'], myexpenditure['cumtotal']))
            expenditure = myexpenditure['expenditure']
            #cumTotal = myexpenditure['cumtotal']
            if myexpenditure['isValid']:
                expenditure.save()
                cumtotal=getInvoiceTotal2(invoice)
                print("total before update={} cumtotal={}".format(invoice.Total_amount,cumtotal))
                invoice.Total_amount=cumtotal
                invoice.save()
                #invoice.Total_amount = cumTotal
                #invoice.save()

           #ivt.delete()
        data['form_is_valid'] = True
        dppitems = Expenditure_details.objects.all()
        data['html_ivt_list'] = render_to_string('pac/includes/expenditures/partial_expenditures_list.html', {
            'invoices': dppitems
        })
    else:
        form = Expenditure_details_Edit_Forms(instance=ivt)
        context = {'ivt': ivt,'form':form}
        data['html_form'] = render_to_string('pac/includes/expenditures/partial_ivt_edit.html', context, request=request)
    return JsonResponse(data)
@login_required
def DeleteExpenditure(request, pk):
    ivt = get_object_or_404(Expenditure_details, pk=pk)
    invoices = list(Invoice_details.objects.filter(expenditure_details__pk=pk))
    invoice = invoices[0]
    data = dict()
    if request.method == 'POST':
        ivt.delete()
        cumtotal = getInvoiceTotal2(invoice)
        invoice.Total_amount=cumtotal
        invoice.save()
        data['form_is_valid'] = True
        dppitems = Expenditure_details.objects.all()
        data['html_ivt_list'] = render_to_string('pac/includes/expenditures/partial_expenditures_list.html', {
            'invoices': dppitems
        })
    else:
        context = {'ivt': ivt}
        data['html_form'] = render_to_string('pac/includes/expenditures/partial_ivt_delete.html', context, request=request)
    return JsonResponse(data)


@login_required
def expenditure_list(request):
    # contracts = Contract.objects.all()
    # civts = Contract.objects.all()
    dppitems=Dpp_allocation.objects.all()
    invoices = Expenditure_details.objects.all()
    fyears=FinancialYear.objects.all()
    months=["ALL",7,8,9,10,11,12,1,2,3,4,5,6]
    return render(request, 'pac/expenditure_list.html', {'invoices': invoices,'fyears':fyears,'dppitems':dppitems,'months':months})
@login_required
def expenditure_list_sort_by_fy(request, pk):
    myyear=FinancialYear.objects.get(pk=pk)
    #myyear=FinancialYear.get
    print(myyear)
    #dppitems =Expenditure_details.objects.filter(budget_allocation__financial_year=pk)
    #allocations=Budget_allocation.objects.filter(Financial_year=myyear)
    #print(allocations)
    dppitems = Expenditure_details.objects.filter( Budget_allocation__Financial_year=myyear)
    print(dppitems)

    data = dict()
    data['html_ivt_list'] = render_to_string('pac/includes/expenditures/partial_expenditures_list.html', {
        'invoices': dppitems
    })

    return JsonResponse(data)
def expenditure_list_sort_by_invoice(request,pk):
    invoice=get_object_or_404(Invoice_details,pk=pk)
    invoices = Expenditure_details.objects.filter(Invoice_details=invoice)
    return render(request, 'pac/expenditure_list_invoice_wise.html', {'invoices': invoices})
def expenditure_list_sort_by_all(request):
    data=dict()
    year_id=request.GET['fy']
    month=request.GET['month']
    ecode=request.GET['ecode']
    fy=FinancialYear.objects.get(pk=year_id)
    invoices=Expenditure_details.objects.filter(Budget_allocation__Financial_year=fy)
    if month !="ALL":
        invoices=invoices.filter(Invoice_details__Month=month)
    if ecode !="ALL":
        invoices=invoices.filter(Budget_allocation__Dpp_allocation__Ecode=ecode)
    print("FY={} month={} ecode={}".format(year_id,month,ecode))
    #dppitems = Expenditure_details.objects.all()
    data['html_ivt_list'] = render_to_string('pac/includes/expenditures/partial_expenditures_list.html', {
        'invoices': invoices
    })
    return JsonResponse(data)

"""  
#################################################################################################################
#################################################################################################################
#################################################################################################################

"""
from .auxilaryquery import createProgressReport
from reportlab.pdfgen import canvas
from django.core.files.storage import FileSystemStorage
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from django.core.files.storage import FileSystemStorage
@login_required
def progressReport(request):
    report_pdf = createProgressReport()


    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline;filename="somefilename.pdf" '
    response.write(report_pdf)
    return response

"""  
#################################################################################################################
#################################################################################################################
Building project progress dash board
#################################################################################################################
#################################################################################################################
"""
def dashboardCategory(request):
    return render (request,'pac/dashboard_category.html',{})



#expenditure_list_sort_by_invoice

"""    
def list_DPP_Intervention(request):
    haors = Haor.objects.all()
    ivts = DPP_Intervention.objects.all().order_by('worktype_id','worktype_id','start_chainage')
    return render(request, 'progress/edit_dpp_intervention2.html', {'ivts': ivts, 'haors': haors})

#context={}
#return render(request, 'pac/add_edit_drop_progress_item.html', context)
    
    #return HttpResponse(html)
"""