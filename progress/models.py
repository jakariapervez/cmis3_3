from __future__ import unicode_literals



from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
class District(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f' {self.name}'

class Division(models.Model):
    division_name=models.CharField(max_length=100)
    district=models.ForeignKey('District',on_delete=models.SET_NULL,null=True)
    div_address=models.CharField(max_length=250,null=True,blank=True)
    div_phone=PhoneNumberField(null=True,blank=True)
    #address=AddressField()

    def __str__(self):
        return f' {self.division_name} {self.div_address}'
class Contractor(models.Model):
    farm_name=models.CharField(max_length=200)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    address=models.CharField(max_length=250,null=True,blank=True)
    tradelicense=models.CharField(max_length=10,blank=True,null=True)
    Vat_registration=models.CharField(max_length=11,blank=True,null=True)
    TIN_No=models.CharField(max_length=12,blank=True,null=True)
    egp_id=models.CharField(max_length=14,blank=True)
    national_id=models.ImageField(null=True,blank=True)
    def __str__(self):
        return f' {self.farm_name} '
class Haor(models.Model):
    Old ='Old'
    New= 'New'
    Types = (
        (Old, 'Rehablitation'),
        (New, 'New Haor'),    )

    name=models.CharField(max_length=100)
    area=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=8)
    project_type=models.CharField(max_length=50,choices=Types)
    population=models.DecimalField(max_digits=8,decimal_places=0,blank=True,null=True,default=0)

    def __str__(self):
        return f' {self.name},{self.project_type},'
class WorkType(models.Model):
    Types=[('EMB','Embankment'),('SUBEMB', 'Submersible,Embankment'),('EXKHL','Khal Rexcavation'),('EXRIV','River Reexcavation'),('REG','Regulator'),('CASW','Cause Way'),
           ('IRIN','Irigation Inlet'),('WMGO','WMG Office'),('BOXSL','Box Sluice')]
    wtype=models.CharField(max_length=30,choices=Types)
    def __str__(self):
        return f' {self.wtype}'
# Create your models here.
class ContractComponent(models.Model):
    Types=[('A','A'),('B', 'B'),('C','C'),('D','D'),('E','E'),('F','F'),
           ('G','G'),('H','H'),]
    component_name=models.CharField(max_length=30,choices=Types)
    def __str__(self):
        return f' {self.component_name}'
# Create your models here.
class Contract(models.Model):
    #Package name
    package_short_name=models.CharField(max_length=200,default='xxx')
    package_detail_name=models.CharField(max_length=1000,default='xxx')
    contractor_short_name=models.CharField(max_length=200,default='xxx')
    #parties
    division_id=models.ForeignKey(Division,on_delete=models.SET_NULL,null=True)
    contractor_id=models.ForeignKey(Contractor,on_delete=models.SET_NULL,null=True,blank=True)
    partner_contractor1_id=models.ForeignKey(Contractor,on_delete=models.SET_NULL,null=True,related_name='partner_contractor1_id',blank=True)
    partner_contractor2_id = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True,related_name='partner_contractor2_id', blank=True)
    #dates
    start_date=models.DateField(default=timezone.now)
    finish_date=models.DateField(default=datetime.now)
    extended_date=models.DateField(null=True,blank=True)
    #contract amount
    contract_amount=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=13)
    billed_amount = models.DecimalField(null=True, blank=True,decimal_places=2,max_digits=13)
    estimated_amount = models.DecimalField(null=True, blank=True,decimal_places=2,max_digits=13)
    #progress
    physical_progress=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=6)
    financial_progress = models.DecimalField(null=True, blank=True,decimal_places=2,max_digits=6)
    #reporting authority
    #xen_id=models.ForeignKey(Personal,on_delete=models.SET_NULL,null=True,related_name='issuer_id',blank=True)
    xen_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True, related_name='xen_id', blank=True)
    sde_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='sde_id',
                               blank=True)
    so_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='so_id',
                               blank=True)
    fse_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                     related_name='field_engg', blank=True)
    cse_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                          related_name='consultant_engg', blank=True)
    #checker_id = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, related_name='checker_id',blank=True)
    #approver_id = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, related_name='approver_id',blank=True)

    def __str__(self):
        return f'{self.package_short_name}'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        #return reverse('contract_detail', args=[str(self.id)])
        return reverse('contract_detail',args=[str(self.package_id)])
class DPP_Intervention(models.Model):
    contract_status_choices = [("HAVE_CONTRACT", "HAVE_CONTRACT"), ("HAVE_NO_CONTRACT", "HAVE_NO_CONTRACT")]
    work_status_choices = [("OG", "OG"), ("COMP", "COMP"), ("TO_BE_STARTED", "TO_BE_STARTED")]
    haor_id = models.ForeignKey(Haor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=400)
    start_chainage = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    finish_chainage = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    length = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    volume = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    vent_no = models.IntegerField(null=True, blank=True)
    dpp_cost=models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    worktype_id = models.ForeignKey(WorkType, on_delete=models.SET_NULL, null=True, blank=True)
    contract_status = models.CharField(max_length=100, choices=contract_status_choices, null=True, blank=True,
                                       default= "HAVE_NO_CONTRACT")
    work_status = models.CharField(max_length=100, choices=work_status_choices, blank=True, null=True,
                                   default= "OG")

    def __str__(self):
        return f'{self.name}'+ ' in ' +f'{self.haor_id.name}'


class Contract_Intervention(models.Model):
    contract_id=models.ForeignKey(Contract,on_delete=models.SET_NULL,null=True,blank=True)
    dpp_intervention_id=models.ForeignKey(DPP_Intervention,on_delete=models.CASCADE)
    contract_component_id = models.ForeignKey(ContractComponent, on_delete=models.SET_NULL, null=True, blank=True)
    physical_weight = models.DecimalField(blank=True,default=0.10,max_digits=4,decimal_places=3)
    financial_weight = models.DecimalField(blank=True, default=0.10,max_digits=4,decimal_places=3)

    """       
    so_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,
                                  related_name='so', blank=True)
    sde_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                              related_name='sde', blank=True)
    exen_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                              related_name='exen', blank=True)
    site_eng_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='site_engg', blank=True)
    field_eng_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='field_engg', blank=True)
    consultant_eng_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,related_name='consultant_engg', blank=True)
     """

    def __str__(self):
        return f'{self.dpp_intervention_id.name}'




class ProgressItem(models.Model):
    intervention_id=models.ForeignKey(Contract_Intervention,on_delete=models.SET_NULL,null=True,blank=True)
    item_name=models.CharField(max_length=200,default="EW")
    unit=models.CharField(max_length=10)
    quantity=models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    weight=models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=3)
    startdate=models.DateField(default=timezone.now)
    finishdate=models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.item_name}'
from django.contrib.auth.models import User

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True,null=True)
    document = models.ImageField(upload_to='documents/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)

class ConstructionImage(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='structures/%Y/%m/%d/')
    acquisition_date=models.DateTimeField(default=datetime.now)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    structure_id = models.ForeignKey(Contract_Intervention, on_delete=models.CASCADE, null=True, blank=True)


class Progress_Quantity(models.Model):
    progress_item_id=models.ForeignKey(ProgressItem,on_delete=models.SET_NULL,null=True,blank=True)
    date=models.DateField(default=timezone.now)
    quantity=models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    document_id=models.ForeignKey(ConstructionImage,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f'{self.quantity}'

class ProgresSchedule(models.Model):
    progress_item_id = models.ForeignKey(ProgressItem, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=datetime.now)
    quantity = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)

    def __str__(self):
        return f'{self.quantity}'




