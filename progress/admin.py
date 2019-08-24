from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import District,Division
admin.site.register(District)
@admin.register(Division)
class Division_Admin(ImportExportModelAdmin):
    pass
from .models import Haor,WorkType,ContractComponent,DPP_Intervention

admin.site.register(Haor)
@admin.register(WorkType)
class WorkType_Admin(ImportExportModelAdmin):
    pass
admin.site.register(ContractComponent)
@admin.register(DPP_Intervention)
class DPP_Intervention_Admin(ImportExportModelAdmin):
    pass
from .models import Contractor,Contract
@admin.register(Contractor)
class Contractor_Admin(ImportExportModelAdmin):
    pass
@admin.register(Contract)
class Contract_Admin(ImportExportModelAdmin):
    pass
from .models import Contract_Intervention
@admin.register(Contract_Intervention)
class Contrtact_Intervention_Admin(ImportExportModelAdmin):
    pass
from .models import ProgressItem,ConstructionImage,Progress_Quantity
admin.site.register(ProgressItem)
admin.site.register(Progress_Quantity)

admin.site.register(ConstructionImage)


