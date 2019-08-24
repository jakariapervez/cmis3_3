from django import forms
#from .models import DPP_Intervention,Haor,Document,Contract_Intervention,ProgressItem,InvoiceImage
from .models import Dpp_allocation,Budget_allocation
"creating DPP_Intervention_form"
class DPP_intervention_form(forms.ModelForm):
    class Meta:
        model=Dpp_allocation
        fields=('Ecode', 'Description', 'Gob', 'Rpa', 'Dpa','Total')
class Budget_allocation_form(forms.ModelForm):
    class Meta:
        model=Budget_allocation
        fields=( 'Financial_year','Dpp_allocation', 'Gob', 'Rpa', 'Dpa','Total')
from .models import InvoiceImage
class InvoiceImageForm(forms.ModelForm):
    class Meta:
        model = InvoiceImage
        fields = ('description', 'invoice_image','issuing_date', 'uploaded_date',)
from .models import Invoice_details

class Invoice_details_Forms(forms.ModelForm):
    class Meta:
        model=Invoice_details
<<<<<<< HEAD
<<<<<<< HEAD
        fields=('Invoice_no','date','BatchType','Description','Total_amount','document_id', )
=======
        fields=('Invoice_no','date','BatchType','Description','document_id', )
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
=======
        fields=('Invoice_no','date','BatchType','Description','document_id', )
>>>>>>> 65827334fbf1f5d1e3508b179fb305e81b4c3651
        #fields=("__all_")

from .models import Expenditure_details
class Expenditure_details_Forms(forms.ModelForm):
    #date=forms.DateField(required=False)
    class Meta:
        model=Expenditure_details
        #fields=('Gob','Dpa','Rpa','Total','Budget_allocation','date','Invoice_details' )
        fields = ('Gob', 'Dpa', 'Rpa',  'Budget_allocation')
        #widgets = {'Total': forms.NumberInput(attrs={'disabled': True}),'date':forms.DateInput(attrs={'disabled': True}),'Invoice_details':forms.TextInput(attrs={'disabled': True})}




class Expenditure_details_Edit_Forms(forms.ModelForm):
    class Meta:
        model=Expenditure_details
        fields=('Gob','Dpa','Rpa' )
"""    
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
from .models import ConstructionImage

class ConstructionImageForm(forms.ModelForm):
    class Meta:
        model = ConstructionImage
        fields = ('description', 'image','acquisition_date', 'structure_id',)

class ConstructionImageFormEnhanced(ConstructionImageForm):
    class Meta:
        model = ConstructionImage
        fields = ('description', 'image','acquisition_date', 'structure_id',)






class ContractAddForm(forms.ModelForm):
    class Meta:
        model=Contract_Intervention
        #fields=("contract_id","dpp_intervention_id","contract_component_id","so_id","sde_id","exen_id","site_eng_id","field_eng_id","consultant_eng_id")
        fields = ("contract_id", "dpp_intervention_id", "contract_component_id",'physical_weight','financial_weight')
        widgets = {'contract_id': forms.HiddenInput(),"dpp_intervention_id":forms.HiddenInput()}
        #fields = ("contract_component_id", "so_id", "sde_id", "exen_id", "site_eng_id", "field_eng_id", "consultant_eng_id")


class AddProgressItemForm(forms.ModelForm):
    class Meta:
        model=ProgressItem
        #fields=("contract_id","dpp_intervention_id","contract_component_id","so_id","sde_id","exen_id","site_eng_id","field_eng_id","consultant_eng_id")
        #widgets = {'contract_id': forms.HiddenInput(),"dpp_intervention_id":forms.HiddenInput()}
        #fields = ("contract_component_id", "so_id", "sde_id", "exen_id", "site_eng_id", "field_eng_id", "consultant_eng_id")
        fields=("intervention_id","item_name","unit","quantity","weight","startdate","finishdate")
        widgets = {'intervention_id': forms.HiddenInput()}
"""
class ProgressQuantityForm (forms.Form):
    quantity=forms.DecimalField()
    item_id=forms.IntegerField()




