from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app1.models import *
from app1.form import Studentform 


def home(request):
    # d={'name':'Ashi','age':20}
    d=student.objects.all()
    return render(request,'home.html',{'d':d})
def index(request):
    return HttpResponse("hello welcome to this page")
def new(request):
    # a={'name':'je','age':20}
    a=employee.objects.all()
    return render(request,'new.html',{'a':a})
def form1(request):
    form=Studentform()
    if(request.method=='POST'):
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return new(request)
    return render(request,'form1.html',{'form':form})
        
def form2(request):
    if(request.method=='POST'):
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return new(request)
    return render(request,'form2.html')

def form3(request):
    if(request.method=='POST'):
        n=request.POST['n']
        m=request.POST['a']
        s=student.objects.create(name=n,age=m)
    return render(request,'form3.html')    

        



