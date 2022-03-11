from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from webtravelapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def travel(request):
    ucount = traveldb.objects.all().count() 
    ucount1=registerdb.objects.all().count()
    ucount2=contactdb.objects.all().count()   
    return render(request,'index.html',{'ucount':ucount,'ucount1':ucount1,'ucount2':ucount2})
    
def destination(request):
    return render(request,'add_destination.html')

def view(request):
    data=traveldb.objects.all()
    return render(request,'view_destination.html',{'data':data})

def getdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        location=request.POST.get('location')
        image=request.FILES['photo']
        price=request.POST.get('price')
        data=traveldb(name=name,location=location,photo=image,price=price)
        data.save()
        return redirect('view')

def edit(request,sid):
    data=traveldb.objects.filter(id=sid)
    return render(request,'edit.html',{'data':data})

def delete(request,vid):
    data=traveldb.objects.get(id=vid).delete()
    return redirect('view')

def update(request,wid):
    if request.method=='POST':
        name_c=request.POST.get('name')
        location_c=request.POST.get('location')
        try:
            image_r=request.FILES['file']
            fs = FileSystemStorage() 
            file = fs.save(image_r.name, image_r)
        except MultiValueDictKeyError :
            file=traveldb.objects.get(id=wid).photo
        price_c=request.POST.get('price')
        traveldb.objects.filter(id=wid).update(name=name_c,location=location_c,photo=file,price=price_c)
    return redirect('view')

def adminlogin(request):
    return render(request,'adminlogin.html')

def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('travel')
        else:
            return render(request,'adminlogin.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adminlogin')


