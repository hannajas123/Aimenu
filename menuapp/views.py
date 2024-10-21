import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def login(request):
    return render(request,'Login.html')
def login_post(request):
    username = request.POST["username"]
    password = request.POST["password"]
    obj =Login.objects.filter(username=username, password=password)
    if obj.exists():
        obj = Login.objects.get(username=username, password=password)
        if obj.type == 'Admin':
            request.session['lid'] = obj.id
            return HttpResponse('''<script>alert('login successfully');window.location='/AI_menu/Admin_home/'</script>''')
        elif obj.type == 'Kitchen':
            request.session['lid'] = obj.id
            return HttpResponse('''<script>alert('login successfully');window.location='/AI_menu/Kitchen_home/'</script>''')
        elif obj.type == 'ServiceStation':
            request.session['lid'] = obj.id
            return HttpResponse('''<script>alert('login successfully');window.location='/AI_menu/Servicestn_home/'</script>''')
        elif obj.type == 'Cashier':
            request.session['lid'] = obj.id
            return HttpResponse('''<script>alert('login successfully');window.location='/AI_menu/Cashier_home/'</script>''')
    return HttpResponse('''<script>alert('Invalid username or password');window.location='/AI_menu/login/'</script>''')

def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/AI_menu/login/'</script>''')
################################################Admin#################################################################
def Admin_home(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'AdminHomeindex.html')


def Admin_change_pswd(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Login.objects.get(id=request.session['lid'])
    return render(request,'Admin/Admin_changepwsd.html')
def Admin_change_pswd_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    pass1 = request.POST["frstpwd"]
    pass2 = request.POST["currentpswd"]
    obj = Login.objects.get(id=request.session['lid'])
    print(pass1)
    print(obj.password)
    if obj.password == pass2:
        obj.password = pass1
        obj.save()
        return HttpResponse("<script>alert('You changed password');window.location='/AI_menu/login/'</script>")
    else:
        return HttpResponse("<script>alert('You cannot change password');window.location='/AI_menu/Admin_change_pswd/'</script>")


def Add_Staff(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'Admin/Add_Staff.html')
def Add_staff_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    name=request.POST["staffname"]
    gender=request.POST["gender"]
    dob=request.POST["dob"]
    phone=request.POST["phone"]
    mail=request.POST["email"]
    place=request.POST["place"]
    city=request.POST["city"]
    distrct=request.POST["district"]
    type=request.POST["type"]
    photo=request.FILES["photo"]
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg'
    fn = fs.save(date, photo)
    oo=Login()
    oo.username=mail
    oo.password=phone
    oo.type=type
    oo.save()
    ob=Staff()
    ob.photo=fs.url(date)
    ob.name=name
    ob.gender=gender
    ob.dob=dob
    ob.phone=phone
    ob.email=mail
    ob.place=place
    ob.city=city
    ob.type=type
    ob.district=distrct
    ob.LOGIN_id=oo.id
    ob.save()
    return HttpResponse("<script>alert('You Added a Staff');window.location='/AI_menu/Add_Staff/'</script>")


def View_Staff(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Staff.objects.all()
    return render(request,'Admin/View_staff.html',{'data':res})
def Search_Staff_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    srch=request.POST["search"]
    res=Staff.objects.filter(name__icontains=srch)
    return render(request,'Admin/View_staff.html',{'data':res})
def Edit_Staff(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Staff.objects.get(id=did)
    return render(request,'Admin/Edit_staff.html',{'data':res})
def Edit_staff_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    name = request.POST["staffname"]
    gender = request.POST["gender"]
    dob = request.POST["dob"]
    phone = request.POST["phone"]
    mail = request.POST["email"]
    place = request.POST["place"]
    city = request.POST["city"]
    distrct = request.POST["district"]
    did = request.POST["id1"]
    if "photo" in request.FILES:
        photo = request.FILES["photo"]
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg'
        fn = fs.save(date, photo)
        oo = Login()
        oo.username = mail
        oo.password = phone
        oo.type = 'Staff'
        oo.save()
        ob = Staff.objects.get(id=did)
        ob.photo = fs.url(date)
        ob.name = name
        ob.gender = gender
        ob.dob = dob
        ob.phone = phone
        ob.email = mail
        ob.place = place
        ob.city = city
        ob.type = type
        ob.district = distrct
        ob.LOGIN_id = oo.id
        ob.save()
        return HttpResponse("<script>alert('You Edited  Staff ');window.location='/AI_menu/View_Staff/'</script>")
    else:

        oo = Login()
        oo.username = mail
        oo.password = phone
        oo.type = 'Staff'
        oo.save()
        ob = Staff.objects.get(id=did)
        ob.name = name
        ob.gender = gender
        ob.dob = dob
        ob.phone = phone
        ob.email = mail
        ob.place = place
        ob.city = city
        ob.type = type
        ob.district = distrct
        ob.LOGIN_id = oo.id
        ob.save()
        return HttpResponse("<script>alert('You Edited  Staff ');window.location='/AI_menu/View_Staff/'</script>")

def Delete_staff_post(request,did):
    res=Staff.objects.filter(id=did).delete()
    return HttpResponse("<script>alert('You Deleted  Staff ');window.location='/AI_menu/View_Staff/'</script>")


def Add_Menu(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'Admin/Add_menu.html')
def Add_Menu_post(request):
    itemname = request.POST["itemname"]
    photo = request.FILES["photo"]
    des = request.POST["description"]
    price = request.POST["price"]
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg'
    fn = fs.save(date, photo)
    oo = Menu()
    oo.item_name = itemname
    oo.description = des
    oo.price = price
    oo.photo = fs.url(date)
    oo.save()
    return HttpResponse("<script>alert('You Added  New Menu ');window.location='/AI_menu/Add_Menu/'</script>")
def View_Menu(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Menu.objects.all()
    return render(request,'Admin/View_menu.html',{'data':res})
def Search_Menu_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    srch=request.POST['search']
    res=Menu.objects.filter(item_name__icontains=srch)
    return render(request,'Admin/View_menu.html',{'data':res})
def Edit_Menu(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Menu.objects.get(id=did)
    return render(request,'Admin/Edit_menu.html',{'data':res})
def Edit_Menu_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    itemname = request.POST["itemname"]
    des = request.POST["description"]
    price = request.POST["price"]
    did=request.POST['id1']
    if 'photo'in request.FILES:
        photo = request.FILES["photo"]
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg'
        fn = fs.save(date, photo)
        oo = Menu.objects.get(id=did)
        oo.item_name = itemname
        oo.description = des
        oo.price = price
        oo.photo = fs.url(date)
        oo.save()
        return HttpResponse("<script>alert('You Edited the Menu ');window.location='/AI_menu/View_Menu/'</script>")
    else:
        oo = Menu.objects.get(id=did)
        oo.item_name = itemname
        oo.description = des
        oo.price = price
        oo.save()
        return HttpResponse("<script>alert('You Edited  the Menu ');window.location='/AI_menu/View_Menu/'</script>")
def Delete_Menu_post(request,did):
    res=Menu.objects.get(id=did).delete()
    return HttpResponse("<script>alert('You Edited  the Menu ');window.location='/AI_menu/View_Menu/'</script>")


def Add_Tdyscpcl(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Menu.objects.all()
    return render(request,'Admin/Add_todays_special.html',{'data':res})
def Add_Tdyscpcl_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    tdyspcl=request.POST['special']
    oo=Special_Menu()
    oo.MENU_id=tdyspcl
    oo.save()
    return HttpResponse("<script>alert('You Added  Todays special ');window.location='/AI_menu/Add_Tdyscpcl/'</script>")
def View_Tdyscpcl(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Special_Menu.objects.all()
    return render(request,'Admin/View_todays_special.html',{'data':res})
def Search_Tdyscpcl_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    srch=request.POST["search"]
    res=Special_Menu.objects.filter(MENU__item_name__icontains=srch)
    return render(request,'Admin/View_todays_special.html',{'data':res})
def Edit_Tdyscpcl(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    oo=Menu.objects.all()
    res=Special_Menu.objects.get(id=did)
    return render(request,'Admin/Edit_todays_special.html',{'data':res,'data1':oo})
def Edit_Tdyscpcl_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    did=request.POST["id1"]
    tdyspcl = request.POST['special']
    oo = Special_Menu.objects.get(id=did)
    oo.MENU_id = tdyspcl
    oo.save()
    return HttpResponse("<script>alert('You Edited  Todays special ');window.location='/AI_menu/View_Tdyscpcl/'</script>")
def Delete_Tdyscpcl_post(request,did):
    res=Special_Menu.objects.filter(id=did).delete()
    return HttpResponse("<script>alert('You Deleted  Todays special ');window.location='/AI_menu/View_Tdyscpcl/'</script>")


def Add_Table(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'Admin/Add_table.html')
def Add_Table_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    tabno=request.POST["tabno"]
    Seats=request.POST["seats"]
    ob=Table()
    ob.table_no=tabno
    ob.no_of_seats=Seats
    ob.save()
    return HttpResponse("<script>alert('You Added  Tables ');window.location='/AI_menu/Add_Table/'</script>")
def View_Table(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Table.objects.all()
    return render(request,'Admin/View_table.html',{'data':res})
def Search_Table_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    serch=request.POST["search"]
    res=Table.objects.filter(table_no__icontains=serch)
    return render(request,'Admin/View_table.html',{'data':res})
def Edit_Table(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Table.objects.get(id=did)
    return render(request,'Admin/Edit_table.html',{'data':res})
def Edit_Table_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    did=request.POST["id1"]
    tabno = request.POST["tabno"]
    Seats = request.POST["seats"]
    ob = Table.objects.get(id=did)
    ob.table_no = tabno
    ob.no_of_seats = Seats
    ob.save()
    return HttpResponse("<script>alert('You Updated  Tables ');window.location='/AI_menu/View_Table/'</script>")
def Delete_Table_post(request,did):
    res=Table.objects.get(id=did).delete()
    return HttpResponse("<script>alert('You Deleted  Tables ');window.location='/AI_menu/View_Table/'</script>")

def View_customers(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Customer.objects.all()
    return render(request,'Admin/View_customers.html',{'data':res})
def Search_customer(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    srch=request.POST["search"]
    res=Customer.objects.filter(name__icontains=srch)
    return render(request,'Admin/View_customers.html',{'data':res})


def View_complaints(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Complaint.objects.all()
    return render(request,'Admin/View_complaints.html',{'data':res})
def Search_complaints(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromd=request.POST["from"]
    tod=request.POST["to"]
    rs=Complaint.objects.filter(date__range=[fromd,tod])
    return render(request,'Admin/View_complaints.html',{'data':rs})
def Send_Reply(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Complaint.objects.get(id=did)
    return render(request,'Admin/Send_reply.html',{'data':res})
def Send_reply_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    rply=request.POST["reply"]
    did=request.POST["id1"]
    oo=Complaint.objects.get(id=did)
    oo.reply=rply
    oo.status='Replyed'
    oo.save()
    return HttpResponse("<script>alert('You Replyed Successfully ');window.location='/AI_menu/View_complaints/'</script>")


def View_Reports(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_sub.objects.all()
    l=[]
    for i in res:
        if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
            pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
            l.append({'acc_no':pays.acc_no,'pdate':pays.date, 'cname':i.ORDERMAIN.CUSTOMER.name, 'item':i.MENU.item_name,'quantity':i.quantity,'amount':i.ORDERMAIN.amount,'date':i.ORDERMAIN.date})
        else:
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name, 'item': i.MENU.item_name,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount, 'date': i.ORDERMAIN.date})
    return render(request, 'Admin/View_report.html', {'data': l})
def Search_Reports(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromi=request.POST["from"]
    toi=request.POST["to"]

    res=Order_sub.objects.filter(ORDERMAIN__date__range=[fromi,toi])
    l = []
    for i in res:
        if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
            pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
            l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,
                      'item': i.MENU.item_name, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
        else:
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,
                 'item': i.MENU.item_name,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount, 'date': i.ORDERMAIN.date})
    return render(request, 'Admin/View_report.html', {'data': l})


def View_Orders(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_sub.objects.all()
    return render(request,'Admin/View_Orders.html',{'data':res})
def Search_Orders(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromd = request.POST["from"]
    tod = request.POST["to"]
    rs = Order_sub.objects.filter(ORDERMAIN__date__range=[fromd, tod])
    return render(request,'Admin/View_Orders.html',{'data':rs})
##########################################Kitchen#####################################################
def Kitchen_home(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'KitchenHomeindex.html')


def Kitchen_change_pswd(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Login.objects.get(id=request.session['lid'])
    return render(request,'Kitchen/Kitchen_change pswd.html')
def Kitchen_change_pswd_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    pass1 = request.POST["frstpwd"]
    pass2 = request.POST["currentpswd"]
    obj = Login.objects.get(id=request.session['lid'])
    print(pass1)
    print(obj.password)
    if obj.password == pass2:
        obj.password = pass1
        obj.save()
        return HttpResponse("<script>alert('You changed password');window.location='/AI_menu/login/'</script>")
    else:
        return HttpResponse(
            "<script>alert('You cannot change password');window.location='/AI_menu/Kitchen_change_pswd/'</script>")


def kitchen_View_New_Orders_nd_update_status(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_sub.objects.filter(ORDERMAIN__status__icontains='payment completed')
    return render(request,'Kitchen/View_new_orders_nd_update_status.html',{'data':res})
def kitchen_Update_status_Orders(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_main.objects.filter(id=did).update(status="Ready to serve")
    return HttpResponse("<script>alert('You Updated Status');window.location='/AI_menu/kitchen_View_New_Orders_nd_update_status/'</script>")

def kitchen_Search_New_Orders_nd_update_status(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromd = request.POST["from"]
    tod = request.POST["to"]
    rs = Order_sub.objects.filter(ORDERMAIN__date__range=[fromd, tod])
    return render(request,'Kitchen/View_new_orders_nd_update_status.html',{'data':rs})


def Add_timeDelay_details(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    from datetime import datetime
    res=Order_sub.objects.filter(ORDERMAIN__date=datetime.now().date().today())
    return render(request,'Kitchen/Add_time_delay_datails.html',{'data':res})
def time_delay(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'Kitchen/Timedelypost.html',{'data':did})
def Add_timeDelay_details_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    did=request.POST["id1"]
    time=request.POST["time"]
    obj=Order_delay()
    obj.ORDERMAIN=Order_main.objects.get(id=did)
    obj.Time_in_minutes=time
    obj.save()
    print(did)
    return HttpResponse("<script>alert('You Added Time delay');window.location='/AI_menu/Add_timeDelay_details/'</script>")


def View_Reviews(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Reviews.objects.all()
    return render(request,'Kitchen/View_reviews_Customer.html',{'data':res})
def Search_Reviews(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromd = request.POST["from"]
    tod = request.POST["to"]
    rs = Reviews.objects.filter(date__range=[fromd, tod])
    return render(request,'Kitchen/View_reviews_Customer.html',{'data':rs})

########################################Service_Station####################################################
def Servicestn_home(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'ServiceStationHomeIndex.html')


def Service_station_change_pswd(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Login.objects.get(id=request.session['lid'])
    return render(request,'Service_station/Service_stn_changepswd.html')
def Service_station_change_pswd_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    pass1 = request.POST["frstpwd"]
    pass2 = request.POST["currentpswd"]
    obj = Login.objects.get(id=request.session['lid'])
    print(pass1)
    print(obj.password)
    if obj.password == pass2:
        obj.password = pass1
        obj.save()
        return HttpResponse("<script>alert('You changed password');window.location='/AI_menu/login/'</script>")
    else:
        return HttpResponse(
            "<script>alert('You cannot change password');window.location='/AI_menu/Service_station_change_pswd/'</script>")


def View_Completed_Orders(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_sub.objects.filter(ORDERMAIN__status='Served')
    return render(request,'Service_station/View_Completed_orders.html',{'data':res})
def Search_Completed_Orders(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromd = request.POST["from"]
    tod = request.POST["to"]
    rs = Order_sub.objects.filter(ORDERMAIN__date__range=[fromd, tod],ORDERMAIN__status='Served')
    return render(request,'Service_station/View_Completed_orders.html',{'data':rs})

def Allocate_to_serving_staff(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Staff.objects.filter(type='Staff')
    return render(request,'Service_station/Allocate_to_serving_staff.html',{'data':res})
def Allocate_to_serving_staff_post(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Staff.objects.filter(id=did).update(type='ServingStaff')
    return HttpResponse("<script>alert('You Updated the Staff as Serving Staff');window.location='/AI_menu/Allocate_to_serving_staff/'</script>")
def Search_Allocted_Staff_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    srch=request.POST["search"]
    res=Staff.objects.filter(name__icontains=srch,type='Staff')
    return render(request,'Service_station/Allocate_to_serving_staff.html',{'data':res})

def Service_update_Order_status(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_sub.objects.filter(ORDERMAIN__status='Ready to serve')
    return render(request,'Service_station/Update_order_status.html',{'data':res})
def Service_update_Order_status_post(request,did):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Order_main.objects.filter(id=did).update(status='Served')
    return HttpResponse("<script>alert('You Updated the Status');window.location='/AI_menu/Service_update_Order_status/'</script>")
def Service_Search_Oder_complete(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromd = request.POST["from"]
    tod = request.POST["to"]
    rs = Order_sub.objects.filter(ORDERMAIN__date__range=[fromd, tod],ORDERMAIN__status='Ready to serve')
    return render(request,'Service_station/Update_order_status.html',{'data':rs})
#################################################Cashier########################################################
def Cashier_home(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    return render(request,'CashierHomeIndex.html')


def Cashier_change_pswd(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res=Login.objects.get(id=request.session['lid'])
    return render(request,'Cashier/Cashier_changepswd.html')
def Cashier_change_pswd_post(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    pass1 = request.POST["frstpwd"]
    pass2 = request.POST["currentpswd"]
    obj = Login.objects.get(id=request.session['lid'])
    print(pass1)
    print(obj.password)
    if obj.password == pass2:
        obj.password = pass1
        obj.save()
        return HttpResponse("<script>alert('You changed password');window.location='/AI_menu/login/'</script>")
    else:
        return HttpResponse("<script>alert('You cannot change password');window.location='/AI_menu/Cashier_change_pswd/'</script>")


def View_bills(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res = Order_sub.objects.all()
    l = []
    for i in res:
        if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
            pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
            l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,
                      'item': i.MENU.item_name, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
        else:
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,
                 'item': i.MENU.item_name,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount, 'date': i.ORDERMAIN.date})
    return render(request,'Cashier/View_Bills.html',{'data': l})
def Search_View_bills(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromi = request.POST["from"]
    toi = request.POST["to"]

    res = Order_sub.objects.filter(ORDERMAIN__date__range=[fromi, toi])
    l = []
    for i in res:
        if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
            pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
            l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,
                      'item': i.MENU.item_name, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
        else:
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,
                 'item': i.MENU.item_name,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount, 'date': i.ORDERMAIN.date})
    return render(request,'Cashier/View_Bills.html', {'data': l})


def View_pament_reports(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    res = Order_sub.objects.all()
    l = []
    for i in res:
        if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
            pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
            l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,
                      'item': i.MENU.item_name, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
        else:
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,
                 'item': i.MENU.item_name,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount, 'date': i.ORDERMAIN.date})
    return render(request,'Cashier/View_payment_reports.html',{'data': l})
def Search_View_pament_reports(request):
    if request.session['lid'] == '':
        return redirect('/AI_menu/login/')
    fromi = request.POST["from"]
    toi = request.POST["to"]

    res = Order_sub.objects.filter(ORDERMAIN__date__range=[fromi, toi])
    l = []
    for i in res:
        if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
            pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
            l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,
                      'item': i.MENU.item_name, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
        else:
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,
                 'item': i.MENU.item_name,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount, 'date': i.ORDERMAIN.date})
    return render(request,'Cashier/View_payment_reports.html',{'data': l})

#######################################customer.......Flutter.........###############################################
def customerlogin_post(request):
    username = request.POST['username']
    password = request.POST['password']
    lobj = Login.objects.filter(username=username, password=password)
    if lobj.exists():
        lobjj = Login.objects.get(username=username, password=password)
        if lobjj.type == 'Customer':
            lid = lobjj.id

            return JsonResponse({'status':'ok', 'lid': str(lid)})
        else:
         return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status': 'no'})
def Cust_Changepassword(request):
    lid=request.POST["lid"]
    cpassword=request.POST["currentpassword"]
    npassword=request.POST["newpassword"]
    if Login.objects.filter(id=lid,password=cpassword).exists():

     obj=Login.objects.get(id=lid)
     obj.password=npassword
     obj.save()
     return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'no'})
def Cust_complaint_post(request):
    lid = request.POST["lid"]
    from datetime import datetime
    date = datetime.now().date().today()
    complaint = request.POST["complaint"]
    status = "pending"
    reply = 'pending'
    time= datetime.now().strftime('%H:%M:%S')
    cobj = Complaint()
    cobj.date = date
    cobj.complaints = complaint
    cobj.time=time
    cobj.status = status
    cobj.reply = reply
    cobj.CUSTOMER =Customer.objects.get(LOGIN_id=lid)
    cobj.save()
    return JsonResponse({'status': 'ok'})
def view_reply(request):
    lid = request.POST['lid']
    sf = Complaint.objects.filter(CUSTOMER__LOGIN_id=lid)
    l = []
    for i in sf:
         l.append({'id':i.id,'date': i.date, 'complaint':i.complaints,'status': i.status, 'reply': i.reply,'time':i.time})
    return JsonResponse({'status': 'ok', 'data': l})
def Cust_Register(request):
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        city = request.POST['city']
        # pin = request.POST['pin']
        # district = request.POST['district']
        # from datetime import datetime
        # date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
        photo = request.POST['photo']

        import datetime
        import base64
        #
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        a = base64.b64decode(photo)
        fh=open("C:\\Users\\Microsoft\\PycharmProjects\\AI_menu\\media\\"+date+".jpg","wb")
        # fh = open("C:\\Users\\user\\PycharmProjects\\Ai_diet\\media\\" + date + ".jpg", "wb")
        # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
        path = "/media/" + date + ".jpg"
        fh.write(a)
        fh.close()
        # fs=FileSystemStorage()
        # fn=fs.save(date,photo)
        # path=fs.url(date)
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # blood = request.POST['blood']
        # intrest = request.POST['intrest']

        # res = Login.objects.get(username!= email)
        # if res.exists():
        if password == cpassword:
            lobj = Login()
            lobj.username = email
            lobj.password = cpassword
            lobj.type = 'Customer'
            lobj.save()

            uobj = Customer()
            uobj.name = name
            uobj.dob = dob
            uobj.gender = gender
            uobj.phone = phone
            uobj.email = email
            uobj.photo = path
            uobj.place = place

            uobj.city = city

            uobj.LOGIN = lobj
            uobj.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'no'})

def Cust_View_Menu(request):
    res = Menu.objects.all().order_by('-positive', 'neutral', 'negative')
    l = []
    for i in res:
        l.append({'id': i.id, 'itemname': i.item_name, 'photo': i.photo,'price':i.price,'description':i.description})
    return JsonResponse({'status': 'ok', 'data': l})

def Cust_View_todays_special(request):
    res = Special_Menu.objects.all().order_by('-MENU__positive', 'MENU__neutral', 'MENU__negative')
    l = []
    for i in res:
        l.append(
            {'id': i.MENU.id, 'itemname': i.MENU.item_name, 'photo': i.MENU.photo, 'price': i.MENU.price, 'description': i.MENU.description})
    return JsonResponse({'status': 'ok', 'data': l})


# def Cust_View_reviews(request):
#     mid = request.POST['mid']
#     sf = Reviews.objects.filter(MENU_id=mid)
#     l = []
#     for i in sf:
#         rvAvg = Reviews.objects.aggregate(Avg('rating'))
#         l.append({'id': i.id, 'date': i.date, 'review': i.review, 'rating': str(rvAvg['rating__avg']), 'menu': i.MENU.item_name,'mid':i.MENU.id,
#                   'time': i.time})
#     return JsonResponse({'status': 'ok', 'data': l})


def Cust_View_reviews(request):
    mid = request.POST['mid']
    result=Reviews.objects.filter(MENU_id=mid)
    print(result)
    list_rev=[]
    for i in result:
        list_rev.append(i.review)
    p, n, nu = sent(list_rev)
    print("Scor ", p,n)
    stat=["Positive", "Negative"]
    if p==0 and n==0:
        p=1
    scor = [p, n]
    fname=piechart(stat, scor)
    l = []
    for i in result:
        rvAvg = Reviews.objects.aggregate(Avg('rating'))
        l.append({'id': i.id, 'date': i.date, 'review': i.review, 'rating': str(rvAvg['rating__avg']),
                  'menu': i.MENU.item_name, 'mid': i.MENU.id,
                  'time': i.time})

    return JsonResponse({'status': 'ok', 'data': l, 'fname':fname})


import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
def piechart(stat, scor):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Sale', 'Purchase'
    # sizes = [random.randint(10,30), random.randint(30,50)]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(scor, explode=explode, labels=stat, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    dt=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename=dt+".png"
    plt.savefig('C:\\Users\\Microsoft\\PycharmProjects\\AI_menu\\media\\graph\\'+filename, dpi=100)
    return filename


def sent(k):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    pstv=0
    ngtv=0
    ntl=0
    sid = SentimentIntensityAnalyzer()
    for sentence in k:

        ss = sid.polarity_scores(sentence)
        a = float(ss['pos'])
        b = float(ss['neg'])
        c = float(ss['neu'])
        print(a,b,c)
        if a==0.0 and b==0.0:
            ntl=ntl+1
        if a > b:

                pstv = pstv + 1

        else:

                ngtv=ngtv+1

    return pstv,ngtv,ntl






def Cust_add_tocart(request):
        mid = request.POST['mid']
        cd = Menu.objects.get(id=mid)
        print(cd.photo)
        return JsonResponse({'status': 'ok', 'mid': cd.id, 'menu': cd.item_name, 'photo': cd.photo, 'price': cd.price,
                             'description': cd.description})

def AddCart_post(request):
    lid=request.POST['lid']
    mid=request.POST['mid']
    quantity=request.POST['quantity']
    ob=Cart()
    ob.MENU=Menu.objects.get(id=mid)
    ob.CUSTOMER=Customer.objects.get(LOGIN_id=lid)
    ob.quantity=quantity
    ob.save()
    return JsonResponse({'status':'ok'})

def Cust_View_order_status(request):
    lid = request.POST['lid']
    res = Order_sub.objects.filter(ORDERMAIN__CUSTOMER__LOGIN=lid)
    l = []
    for i in res:
        if Payment.objects.filter(ORDERMAIN_id=i.ORDERMAIN.id).exists():
            pays = Payment.objects.get(ORDERMAIN_id=i.ORDERMAIN.id)
            l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,'status':i.ORDERMAIN.status,
                      'item': i.MENU.item_name,'id':i.MENU.id, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
        else:
            # pays = Payment.objects.get(ORDERMAIN_id=i.ORDERMAIN.id)
            l.append(
                {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,'status':i.ORDERMAIN.status,
                 'item': i.MENU.item_name,'id':i.MENU.id,
                 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                 'date': i.ORDERMAIN.date})
    return JsonResponse({'status': 'ok', 'data': l})

def Cust_View_bill(request):
    lid = request.POST['lid']
    res = Order_sub.objects.filter(ORDERMAIN__CUSTOMER__LOGIN=lid)
    l = []
    for i in res:
            if Payment.objects.filter(ORDERMAIN=i.ORDERMAIN).exists():
                pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
                l.append({'acc_no': pays.acc_no, 'pdate': pays.date, 'cname': i.ORDERMAIN.CUSTOMER.name,
                          'item': i.MENU.item_name, 'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                          'date': i.ORDERMAIN.date})
            else:
                 # pays = Payment.objects.get(ORDERMAIN=i.ORDERMAIN)
                 l.append(
                     {'acc_no': 'Not Yet Paid', 'pdate': 'Not Yet Paid', 'cname': i.ORDERMAIN.CUSTOMER.name,
                      'item': i.MENU.item_name,
                      'quantity': i.quantity, 'amount': i.ORDERMAIN.amount,
                      'date': i.ORDERMAIN.date})
    return JsonResponse({'status': 'ok','data': l})

def Cust_Payment(request):
        lid = request.POST['lid']
        total = request.POST['total']
        Cardno = request.POST['cardno']
        Cardholder = request.POST['cardholdername']
        Cvv = request.POST['cvv']
        Expirydate = request.POST['expirydate']

        if Bank.objects.filter( cardno=Cardno, cardholder=Cardholder, Cvv=Cvv, expirydate=Expirydate).exists():
            res = Cart.objects.filter(CUSTOMER__LOGIN_id=lid)
            # for i in res:
            #     print(i)
            res2 = Cart.objects.filter(CUSTOMER__LOGIN_id=lid)
            boj = Order_main()
            boj.CUSTOMER = Customer.objects.get(LOGIN_id=lid)
            boj.status = 'Payment Completed'
            boj.date = datetime.datetime.now().date().today()
            boj.amount = total
            boj.save()

            # res3 =
            for j in res2:
                print(j)
                bs = Order_sub()
                bs.ORDERMAIN_id = boj.id
                bs.MENU_id = j.MENU.id
                bs.quantity = j.quantity
                bs.save()

            Cart.objects.filter(CUSTOMER__LOGIN_id=lid).delete()
            boj = Order_main.objects.get(id=boj.id)
            boj.amount = total
            boj.save()

            accno=Bank.objects.get( cardno=Cardno, cardholder=Cardholder, Cvv=Cvv, expirydate=Expirydate).accno
            oo=Payment()
            oo.ORDERMAIN_id=boj.id
            oo.acc_no=accno
            oo.date=datetime.datetime.now().date().today()
            oo.save()

            #
            # for i in
            return JsonResponse({ 'status': "ok"})
        else:
            return JsonResponse({"status": "no"})

def Cust_Send_reviews(request):
    lid = request.POST["lid"]
    mid=request.POST["mid"]
    from datetime import datetime
    date = datetime.now().date().today()
    review = request.POST["review"]
    rating = request.POST["rating"]
    time = datetime.now().strftime('%H:%M:%S')
    list_rev=[]
    list_rev.append(review)
    p, n, nu = sent(list_rev)
    print("Scor ", p,n, nu)
    stat=["Positive", "Negative", "Neutral"]
    if p==0 and n==0:
        p=1
    scor = [p, n, nu]
    print(scor)
    cobj = Reviews()
    cobj.date = date
    cobj.review = review
    cobj.time = time
    cobj.rating = rating
    cobj.MENU_id=mid
    cobj.CUSTOMER = Customer.objects.get(LOGIN_id=lid)
    Menu.objects.filter(id=mid).update(positive=+p, negative=+n, neutral=+nu)
    cobj.save()
    return JsonResponse({'status': 'ok'})

def Cust_View_cart(request):
    lid = request.POST['lid']
    res = Cart.objects.filter(CUSTOMER__LOGIN=lid)

    l = []
    total=0
    for i in res:
        total+=(float(i.MENU.price)*float(i.quantity))
        l.append(
            {'id': i.id, 'menu': i.MENU.item_name, 'photo': i.MENU.photo, 'price': i.MENU.price, 'description': i.MENU.description,'quantity':i.quantity})
    return JsonResponse({'status': 'ok', 'data': l, 'total':total})

