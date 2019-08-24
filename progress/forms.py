from django import forms
from .models import DPP_Intervention,Haor,Document,Contract_Intervention,ProgressItem
"creating DPP_Intervention_form"
class DPP_intervention_form(forms.ModelForm):
    class Meta:
        model=DPP_Intervention
        fields=('haor_id', 'worktype_id', 'name', 'start_chainage', 'finish_chainage','length','volume','vent_no', 'dpp_cost')
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
class ProgressQuantityForm (forms.Form):
    quantity=forms.DecimalField()
    item_id=forms.IntegerField()




