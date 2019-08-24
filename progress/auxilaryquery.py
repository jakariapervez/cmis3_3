from .models import Contract_Intervention,DPP_Intervention,ProgressItem

"""   
intervention_id = models.ForeignKey(Contract_Intervention, on_delete=models.SET_NULL, null=True, blank=True)
item_name = models.CharField(max_length=200, default="EW")
unit = models.CharField(max_length=10)
quantity = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
weight = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
startdate = models.DateField(default=timezone.now)
finishdate = models.DateField(default=timezone.now)

"""
def progresItemEmb(civt):
    length=civt.dpp_intervention_id.length
    volume=civt.dpp_intervention_id.volume
    item1=ProgressItem( intervention_id=civt,item_name="Earth work in filling",unit="Cum",quantity=volume,weight=0.85)
    item1.save()
    item2 = ProgressItem(intervention_id=civt, item_name="Close Turfing", unit="sqm", quantity=0,
                         weight=0.15)
    item2.save()
    item3 = ProgressItem(intervention_id=civt, item_name="Length Completion", unit="Km", quantity=length,
                         weight=0.00)
    item3.save()
def progresItemKhal(civt):
    length=civt.dpp_intervention_id.length
    volume=civt.dpp_intervention_id.volume
    item1=ProgressItem( intervention_id=civt,item_name="Earth work in cutting",unit="Cum",quantity=volume,weight=0.85)
    item1.save()

    item3 = ProgressItem(intervention_id=civt, item_name="Length Completion", unit="Km", quantity=length,
                         weight=0.00)
    item3.save()



def progresItemRiver(civt):
    length = civt.dpp_intervention_id.length
    volume = civt.dpp_intervention_id.volume
    item1 = ProgressItem(intervention_id=civt, item_name="Earth work in cutting", unit="Cum", quantity=volume,
                         weight=0.85)
    item1.save()

    item3 = ProgressItem(intervention_id=civt, item_name="Length Completion", unit="Km", quantity=length,
                         weight=0.00)
    item3.save()

def progresItemReg(civt):
    item1 = ProgressItem(intervention_id=civt, item_name="Earth work in Foundation Excavation", unit="Cum", quantity=5208.35,
                         weight=0.05)
    item1.save()
    item2 = ProgressItem(intervention_id=civt, item_name="Sheet Pile Driving", unit="meter", quantity=134.68,
                         weight=0.15)
    item2.save()

    item3 = ProgressItem(intervention_id=civt, item_name="CC Block manufacturing", unit="Nos", quantity=13344,
                         weight=0.20)
    item3.save()
    item4= ProgressItem(intervention_id=civt, item_name="Foundation and Apron Construction", unit="Cum", quantity=152.89,
                         weight=0.20)
    item4.save()
    item5 = ProgressItem(intervention_id=civt, item_name="Barrel and Wall Construction", unit="cum", quantity=121.79,
                         weight=0.20)
    item5.save()
    item6 = ProgressItem(intervention_id=civt, item_name="Diversion channel and Approach Embankment", unit="cum", quantity=11022.13,
                         weight=0.10)
    item6.save()
    item7 = ProgressItem(intervention_id=civt, item_name="Loose Apron", unit="sqm", quantity=326.18,weight=0.05)

    item7.save()
    item8= ProgressItem(intervention_id=civt, item_name="Gate Installation", unit="Nos", quantity=2, weight=0.05)

    item8.save()

def creteProgressItem(civt):
    """
    intervention_id=civt
    item_name="Earth Work in Foundation"
    unit="Cum"
    quantity=1000
    weight=0.15
    item1=ProgressItem( intervention_id=civt,item_name=item_name,unit=unit,quantity=quantity,weight=weight)
 Types=[('EMB','Embankment'),('SUBEMB', 'Submersible,Embankment'),('EXKHL','Khal Rexcavation'),('EXRIV','River Reexcavation'),('REG','Regulator'),('CASW','Cause Way'),
           ('IRIN','Irigation Inlet'),('WMGO','WMG Office'),('BOXSL','Box Sluice')]
    item1.save()  """
    if(civt.dpp_intervention_id.worktype_id.wtype=="REG"):
        print("this item is")
        progresItemReg(civt)
    elif civt.dpp_intervention_id.worktype_id.wtype=="BOXL":
        progresItemReg(civt)
    elif civt.dpp_intervention_id.worktype_id.wtype=="CASW":
        progresItemReg(civt)
    elif  civt.dpp_intervention_id.worktype_id.wtype=="IRIN":
        progresItemReg(civt)
    elif civt.dpp_intervention_id.worktype_id.wtype == "EMB":
        progresItemEmb(civt)
    elif civt.dpp_intervention_id.worktype_id.wtype== "SUBEMB":
        progresItemEmb(civt)
    elif civt.dpp_intervention_id.worktype_id.wtype == "EXKHL":
        progresItemKhal(civt)
    elif civt.dpp_intervention_id.worktype_id.wtype == "EXRIV":
        progresItemRiver(civt)
    else:
        progresItemEmb(civt)




def deleteProgressItem(civt):
    pitems=ProgressItem.objects.filter(intervention_id=civt)
    pitems.delete()

def prepareMultiline(mystr,cpl):
   nos=int(len(mystr)/cpl)

   for i in range(1,nos+1):
       index=cpl*(i)
       mystr=mystr[:index]+chr(10)+mystr[index:]
   return mystr






from .models import Progress_Quantity
def calculateProgressQuantity(pitem,user,mylist):
    pquantity=list(Progress_Quantity.objects.filter(progress_item_id=pitem,user_id=user).order_by('-date')[:2])
    print(pquantity)
    if pquantity:
        p1=pquantity[0]
        p2=pquantity[1]
        duration=p1.date-p2.date
        q1=float(p1.quantity)
        q2=float(p2.quantity)
        delq=q1-q2
        w=float(mylist[7])
        tq=float(mylist[6])
        print("prev_date={} current_date={} duration={} q1={} q2={} delq={}".format(p1.date, p2.date, duration, q1, q2, delq))
        """   
        tableHeading = ['Sl', 'Prev_Rep_Date', 'curr_date', 'duration' 'Item Name', 'Unit', 'Est_Qua', 'weight', 'Prev_Qua', 'Qua_Curr', 'Qua_Exe_RP', 'Itemised_prog']
         """
        mylist[1]=p2.date
        mylist[2]=p1.date
        mylist[3]=duration
        mylist[8]=q2
        mylist[9]=q1
        mylist[10]=delq
        if tq !=0:
            mylist[11]=round(q1*w/tq,3)
        else:
            mylist[11]=0.0
        print(mylist)
    return mylist
    """    #p1=Progress_Quantity.objects.filter(progress_item_id=pitem,user_id=user).order_by('-date')[2]
    #p2=Progress_Quantity.objects.filter(progress_item_id=pitem,user_id=user).order_by('-date')[1]
    duration=p1.date-p2.date
    prog1=p1.quantiy
    prog2=p2.quantiy
    del_q=prog1-prog2
    print("prev_date={} current_date={} duration={} q1={} q2={} delq={}".foramt(p1.date,p2.date,duration,prog1,prog2,del_q))
    """
    """  
    for p in pquantity:
        print("item={} date={} quantity={}".format(pitem.item_name, p.date,p.quantity))
    """





from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image,Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from django.core.files.storage import FileSystemStorage
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
def createProgressReport(contracts,user):
    """ Basic Setup for Report Lab   """
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer)
    doc.pagesize =landscape(A4)
    flowables = []#overall flowables
    structural_summary=[]#for structural summary
    contract_summary=[]
    sample_style_sheet = getSampleStyleSheet()
    #sample_style_sheet.list()
    """Creating Style for Paragraph  """
    custom_body_style = sample_style_sheet['Heading5']
    #custom_body_style.listAttrs()
    custom_body_style.spaceAfter=0
    custom_body_style.spaceBefore=0

    for contract in contracts:
        structures=Contract_Intervention.objects.filter(contract_id=contract)
        """Variable for Holding Total progress in  structure  """
        #mylist = ['', '', '', '', "Overall Progress",'','', '', '', '', '', '']
        contract_data=[]
        item_progress="itemized"+chr(10)+"progress"
        contract_heading=['sl','name','weight','progress',item_progress]
        contract_data.append(contract_heading)
        contract_sl=1
        contract_sum=0

        myheading2 = "Contract Name : " + contract.package_short_name
        myparagraph2 = Paragraph(myheading2, custom_body_style)
        myparagraph2.hAlign = 'LEFT'
        contract_summary.append(myparagraph2)
        for structure in structures:
            """ Structurl Progress Rreport      """
            contractName=""
            contract_row=[contract_sl,prepareMultiline(structure.dpp_intervention_id.name,25),structure.physical_weight,0,0]
            contract_sl +=1
            """ Adding Header Section For Report """
            myheading1 = "Haor Name : " + structure.dpp_intervention_id.haor_id.name
            myparagraph1 = Paragraph(myheading1, custom_body_style)
            myparagraph1.hAlign = 'LEFT'

            myheading3="Structure Name : "+structure.dpp_intervention_id.name
            myheading4="Reproting Date : "+"24/3/2019" # Latter A Proper Date Will be Created
            #mystr=contract.package_short_name+"/"+structure.dpp_intervention_id.name

            flowables.append(myparagraph1)

            flowables.append(myparagraph2)
            myparagraph3 = Paragraph(myheading3, custom_body_style)
            myparagraph1.hAlign = 'LEFT'
            flowables.append(myparagraph3)
            myparagraph4 = Paragraph(myheading4,  custom_body_style)
            myparagraph1.hAlign = 'LEFT'
            flowables.append(myparagraph4)
            flowables.append(Spacer(1, 0.25 * cm))
            """ Table Section of the report  """
            pitems=ProgressItem.objects.filter(intervention_id=structure)
            mydata=[]
            iprog="item"+chr(10)+ "progress"
            qua_exe="Quan"+chr(10)+"Executed"+chr(10)+"RPeriod"
            tableHeading=['Sl','Pre_date','curr_date','duration','Item Name','Unit','Est_Qua','weight','Prev_Qua','Qua_Curr', qua_exe,iprog]
            mydata.append(tableHeading)
            sl=1
            sum=0.0
            total_structural = ['', '', '', '', "Overall Progress", '', '', '', '', '', '', '']
            for pitem in pitems:
                iname=prepareMultiline(pitem.item_name,25)
                mylist=[sl,'','','',iname, pitem.unit,pitem.quantity,pitem.weight,'','','',0]
                mylist=calculateProgressQuantity(pitem,user,mylist)
                mydata.append(mylist)
                sl+=1
                sum+=float(mylist[11])
                print("total for={}".format(mylist[11]))
            total_structural[11]=sum
            mydata.append(total_structural)
            colwidth=[1.0*cm,1.8*cm,1.8*cm,1.8*cm,4.9*cm,2.0*cm,2.2*cm,2.2*cm,2.2*cm,2.0*cm,2.0*cm,2.0*cm]
            t = Table(mydata,repeatRows=1,colWidths=colwidth)
            t.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black),]))
            t.hAlign = 'LEFT'
            #t.wrapOn()
            flowables.append(t)
            flowables.append(Spacer(1, 0.5* cm))
            contract_row[3]= total_structural[11]
            contract_row[4]=float(contract_row[3])*float(contract_row[2])
            contract_sum +=contract_row[4]
            contract_data.append(contract_row)
        total_contract=['',prepareMultiline('Overall physical Progress',60),'','',contract_sum ]
        contract_data.append(total_contract)
        contract_colwidth=[1.0*cm,12*cm,3*cm,3*cm,4*cm]
        t_contract=Table(contract_data,repeatRows=1,colWidths=contract_colwidth)
        t_contract.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black), ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))
        t_contract.hAlign='LEFT'
        contract_summary.append(t_contract)



    signature_table_data=[]
    #myheading1 = "This is a test paragraph"
    #myparagraph1 = Paragraph(myheading1, custom_body_style)
    for item in reversed(contract_summary):
        flowables.insert(0,item)
    #custom_body_style.listAttrs()
    #sample_style_sheet.list()



    """
    item_name = models.CharField(max_length=200, default="EW")
    unit = models.CharField(max_length=10)
    quantity = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    weight = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=13)
    startdate = models.DateField(default=timezone.now)
    finishdate = models.DateField(default=timezone.now)



    
    styles = getSampleStyleSheet()
    Story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("This is Paragraph number %s.  " % i) * 20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))
    """
    doc.build(flowables)

    pdf_value = pdf_buffer.getvalue()
    pdf_buffer.close()
    return pdf_value


