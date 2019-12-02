from django.shortcuts import render
from django.http import HttpResponse
from cableadmin.models import collectors
from cableadmin.models import Manager,customers
def managerlogin(request):
    users=customers.objects.all() 
    gts=collectors.objects.all()
    if request.method=="POST" and "mlogin" in request.POST:
        print("hey")
        a=request.POST.get('username')
        b=request.POST.get('password')
        au=Manager.objects.filter(manager_id=a)
        for i in au:
            print(i.password)
            if i.password==b:
                return render(request,'manager/manageraccess.htm',{"users":users,"gts":gts})
            else:
                return HttpResponse("<h1>invalid login credentials<h1>")
    if request.method=="POST" and "getcoll" in request.POST:
        a=request.POST.get('cid')
        print(a)
        gt=collectors.objects.filter(collector_id=a)
        return render(request,'manager/manageraccess.htm',{"users":users,"gts":gts,"gt":gt})
    if request.method=="POST" and "addcollector" in request.POST:
        collect=collectors()
        collect.collector_id=request.POST.get('cid')
        collect.collector_name=request.POST.get('cn')
        collect.area_id=request.POST.get('caid')
        collect.save()
        return render(request,'manager/manageraccess.htm',{"users":users,"gts":gts})
    return render(request,'manager/managerlogin.htm')
