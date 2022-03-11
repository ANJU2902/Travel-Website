from django.shortcuts import render,redirect
from django.http import HttpResponse
from travelapp.models import*
from webtravelapp.models import contactdb
from webtravelapp.models import registerdb

# Create your views here.
def web(request):
    data=traveldb.objects.all()
    return render(request,'webindex.html',{'data':data})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def getone(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=contactdb(name=name,phone=phone,email=email,subject=subject,message=message)
        data.save()
    return redirect('web')

def message(request):
    data=contactdb.objects.all()
    return render(request,'messages.html',{'data':data})

def register(request):
    return render(request,'registration.html')

def regi(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=registerdb(name=name,email=email,phone=phone,username=username,password=password)
        data.save()
    return redirect('web')

def registrations(request):
    data=registerdb.objects.all()
    return render(request,'registrations.html',{'data':data})

def userlogin(request):
    return render(request,'userlogin.html')


def userin(request):
    if request.method=="POST":
        username_a=request.POST.get('username')
        password_a=request.POST.get('password')
        print(password_a)
        print(username_a)
        if registerdb.objects.filter(username=username_a,password=password_a).exists():
            data=registerdb.objects.filter(username=username_a,password=password_a).values('name','email','phone','id').first()
            request.session['name']=data['name']
            request.session['email']=data['email']
            request.session['phone']=data['phone']
            request.session['username']=username_a
            request.session['password']= password_a
            request.session['id']=data['id']
            return redirect('web')
        else:
            return render(request,'userlogin.html',{'msg':"sorry... invalid username or password"})
    else:
        return redirect('userlogin')
        
def logout(request):
    del request.session['name']
    del request.session['email']
    del request.session['username']
    del request.session['password']
    del request.session['id']
    return redirect('userlogin')



