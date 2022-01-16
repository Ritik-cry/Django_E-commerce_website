from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product,Contact,Orders,Tracker
from json import dumps

# Create your views here.
def shopHome(request):
    allProd = []
    categories = Product.objects.values('category')
    allCat = {items['category'] for items in categories}
    for cat in allCat:
        prod = Product.objects.filter(category=cat)
        allProd.append(prod)
    params = {'allProd' : allProd}
    return render(request,'shop/index.html',params)

def searchMatch(search,item):
    if len(search)>2:
        if (search in item.productName.lower() or search in item.category.lower() or search in item.desc.lower()) :
            return True
        else:
            return False
    else:
        return False

def search(request):
    search = request.GET.get('search','')
    allProd = []
    categories = Product.objects.values('category')
    allCat = {items['category'] for items in categories}
    for cat in allCat:
        prodTemp = Product.objects.filter(category=cat)
        prod = [item for item in prodTemp if searchMatch(search,item)]
        allProd.append(prod)
    products = []
    for item in allProd:
        if len(item)>0:
            products.append(item)
    params = {'allProd' : products}
    return render(request,'shop/search.html',params)

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    if request.method=='POST':
        orderid = request.POST.get('orderid','')
        email = request.POST.get('email','')
        try:
            order = Orders.objects.filter(id=orderid,email=email)
            if len(order)>0:
                update = Tracker.objects.filter(orderId=orderid)
                updates =[]
                for item in update:
                    updates.append({'text':item.trackerDesc,'time':item.timestamp})
                    data = dumps([updates,order[0].items_json],default=str)
                return HttpResponse(data)
            else:
                return HttpResponse('{}')
        except:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        text = request.POST.get('text','')
        contact = Contact(name=name,email=email,phone=phone,text=text)
        contact.save()
        thank = True
        return render(request,'shop/contact.html',{'thank':thank})
    return render(request,'shop/contact.html')

def product(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,'shop/product.html',{'product':product[0]})

def cart(request):
    if request.method=='POST':
        items_json = request.POST.get('items_json','')
        amount = request.POST.get('amount',0)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + "" + request.POST.get('address2','')
        city = request.POST.get('city','')
        phone = request.POST.get('phone','')
        zip_code = request.POST.get('zip_code','')
        order = Orders(items_json=items_json,amount=amount,name=name,email=email,address=address,city=city,phone=phone,zip_code=zip_code)
        order.save()
        update = Tracker(orderId=order.id,trackerDesc='The order has been placed')
        update.save()
        orderId = order.id
        thank = True
        return render(request,'shop/cart.html',{'thank':thank,'orderId':orderId})
    return render(request,'shop/cart.html')