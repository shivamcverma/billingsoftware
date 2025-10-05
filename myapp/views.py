from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import adminlogintbl, additemstbl, customertbl


# Create your views here.
def adminlogin(request):
    return render(request, 'adminlogin.html')

def logincode(request):
    if request.method == "POST":
        a=request.POST.get('email')
        b=request.POST.get('pass')
        data=adminlogintbl.objects.filter(email=a).first()
        if not data:
            return HttpResponse("email not found")
        elif data.password == b:
            request.session['admin']=a
            return redirect('../dashboard')
        else:
            return HttpResponse("password wrong")

    else:
        return redirect("../adminlogin")

def dashboard(request):
    sesid=request.session['admin']
    if not sesid:
        return redirect('../admminlogin')
    return render(request, 'dashboard.html')
def additems(request):
    return render(request, 'additems.html')


def additems_code(request):
    if request.method == "POST":
        a = request.POST.get('Iname')
        b = request.POST.get('Iquantity')
        c = request.POST.get('Iprice')
        d = request.FILES.get('Ifile')
        additemstbl.objects.create(ItemName=a, Itemquantity=b, Itemprice=c, Ifile=d)
        return HttpResponse("add item successfully")
    else:
        return redirect("../dashboard")

def orderitems(request):
    data=additemstbl.objects.all()
    return render(request, 'orderitems.html', {"show":data})

def orderitemsedit(request,id):
    data=additemstbl.objects.filter(id=id).first()
    return render(request, 'orderitems_edit.html', {"show":data})

def orderitems_update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        a = request.POST.get('name')
        b = request.POST.get('quantity')
        c = request.POST.get('price')
        d = request.FILES.get('file')
        additemstbl.objects.filter(id=id).update(ItemName=a, Itemquantity=b, Itemprice=c, Ifile=d)
        return redirect("../orderitems")
    else:
        return redirect("../")

def orderitems_delete(request,id):
    additemstbl.objects.get(id=id).delete()
    return redirect("../orderitems")


def generatebill_code(request):
    return render(request, 'generatebill_code.html')

def generatecode(request):
    if request.method == "POST":
       a = request.POST.get('cname')
       b = request.POST.get('cnum')
       data=customertbl.objects.filter(customername=a,customermobile=b).first()
       if not data:
          customertbl.objects.create(customername=a,customermobile=b)

          return redirect("../billpage")
       else:

          return redirect("../billpage")

def billpage(request):
    items = additemstbl.objects.all()
    customers = customertbl.objects.all()
    total_price = sum(float(item.Itemprice) * int(item.Itemquantity) for item in items)

    return render(request, 'billpage.html', {"items": items,"total_price": total_price,"show": customers})




