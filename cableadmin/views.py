from django.shortcuts import render
from .models import wifi_properties as wp
from .models import customers as cust
from .models import collectors as coll
from .models import cable_properties as cp
from .wifiform import wifi_form
from .cusforms  import custforms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import redirect
def useroptions(request):
    wifi=wp.objects.all()
    cable=cp.objects.all()
    return render(request,'cableadmin/user-option-page.htm',{"cable":cable,"wifi":wifi})
def usercatalog(request):
    wifi=wp.objects.all()
    cable=cp.objects.all()
    if request.method=='POST' and 'cusloginuc' in request.POST:
        a=request.POST.get("cusiduc")
        b=request.POST.get("cuspassworduc")
        for i in cust.objects.filter(customer_id=a):
            if b==i.password:
                return render(request,"cableadmin/usercatalog.htm",{"user":i,"cable":cable,"wifi":wifi})
    print('hey')
    if request.method=="POST" and 'cabsub' in request.POST:
        opt1=request.POST.get('selectmonthc')
        print(opt1)
        opt2=request.POST.get('selectcable')
        print(opt2)
        cat=request.POST.get('catalog')
        cust.objects.filter(customer_id=cat).update(subscription_cable=opt1,cable_plans=opt2)
        return redirect('useroptions')
    if request.method=="POST" and 'wifisub' in request.POST:
        opt1=request.POST.get('selectmonthw')
        print(opt1)
        opt2=request.POST.get('selectwifi')
        print(opt2)
        cat=request.POST.get('catalog')
        cust.objects.filter(customer_id=cat).update(subscription_wifi=opt1,wifi_plans=opt2)
        return redirect('useroptions')
    return render(request,"cableadmin/user-catalog-login.htm")
def homepage(request):
    return render(request,"cableadmin/homepage.htm")
def userlogin(request):
    if request.method=='POST' and 'cuslogin' in request.POST:
        a=request.POST.get("cusid")
        b=request.POST.get("cuspassword")
        for i in cust.objects.filter(customer_id=a):
            if b==i.password:
                print(i.cable_plans)
                cab=cp.objects.filter(cable_id=i.cable_plans)
                wifi=wp.objects.filter(wifi_id=i.wifi_plans)
                j=''
                for c in cab:
                    j=c.cable_plane_name
                    print(j)
                for w in wifi:
                    print(w.wifi_id)
                    print(j)
                    return render(request,"cableadmin/customerdetails.htm",{"user":i,'w':w,'j':j})
    return render(request,"cableadmin/userlogin.htm")
@login_required(login_url='admin')
def deleteplan(request):
    users=wp.objects.all()
    if request.method=='POST' and 'delwifi' in request.POST:
        print("hey")
        a=request.POST.get("delewifi")
        print(a)
        wp.objects.filter(wifi_id=a).delete()
        return render(request,'cableadmin/deleteplan.htm',{'users':users})
    return render(request,'cableadmin/deleteplan.htm',{'users':users})
@login_required(login_url='login')
def getplan(request):
    forms=wifi_form()
    users=wp.objects.all()
    if request.method=='POST' and 'addwifi' in request.POST:
        forms=wifi_form(request.POST)
        if forms.is_valid():
            forms.save()
            forms=wifi_form()
            return render(request,'cableadmin/getplan.htm',{"forms":wifi_form,"users":users})
    return render(request,'cableadmin/getplan.htm',{"forms":wifi_form,"users":users})
@login_required(login_url='login')
def userdelete(request):
    users=cust.objects.all()
    if request.method=='POST' and 'usedel' in request.POST:
        print("hey")
        a=request.POST.get("t1")
        cust.objects.filter(customer_id=a).delete()
        return render(request,"cableadmin/userdelete.htm",{"users":users})
    return render(request,"cableadmin/userdelete.htm",{"users":users})
@login_required(login_url='login')
def userdetails(request):
    users=cust.objects.all()
    cable=cp.objects.all()
    wifi=wp.objects.all()
    cforms=custforms()
    if request.method=="POST" and "adduser" in request.POST:
        print('hey')
        formses=custforms(request.POST)
        print('hey')
        if formses.is_valid():
            print('hey')
            formses.save()
            return render(request,"cableadmin/userdetails.htm",{"users":users,"cforms":cforms,"wifi":wifi,"cable":cable})
        else:
            print("no ey")

    return render(request,"cableadmin/userdetails.htm",{"users":users,"cforms":cforms,"wifi":wifi,"cable":cable})
@login_required(login_url='login')
def  getinfo(request):
    users=cust.objects.all()
    if request.method=="POST" and "clientinfo" in request.POST:
        print('hey')
        a=request.POST.get("clientidget")
        forms=cust.objects.get(customer_id=a)
        return render(request,"cableadmin/getinfo.htm",{"users":users,"forms":forms})
    if request.method=="POST" and "upclientwifi" in request.POST:
        a1=request.POST.get("clientidget")
        b=request.POST.get("t1")
        c=request.POST.get("t2")
        d=request.POST.get("t3")
        cust.objects.filter(customer_id=a1).update(wifi_plans_id=c,cable_plans_id=d,customer_name=b)
        return render(request,'cableadmin/getinfo.htm',{"users":users})
    return render(request,"cableadmin/getinfo.htm",{"users":users})
@login_required(login_url='login')
def updatearea(request):
    users=cust.objects.all()
    if request.method=='POST' and 'updateclient' in request.POST:
        print("hey")
        a=request.POST.get("upcl")
        b=request.POST.get("upcl2")
        cust.objects.filter(customer_id=a).update(area_id=b)
        return render(request,"cableadmin/updatearea.htm",{"users":users})
    return render(request,"cableadmin/updatearea.htm",{'users':users})
@login_required(login_url='login')
def admindetails(request):
    return render(request,'cableadmin/detailsinadmin.htm')

def logins(request):
    form=AuthenticationForm()
    if request.method=='POST' and 'loginstaff' in request.POST:
        print('hey')
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('hey')
            user=form.get_user()
            login(request,user)
            return render(request,'cableadmin/detailsinadmin.htm')
    return render(request,'cableadmin/adminlogin.htm',{'form':form})
def logouts(request):
    form=AuthenticationForm()
    logout(request)
    return redirect('login')