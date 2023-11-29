from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from app1.models import Book 
from app1.form import *
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
   
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Email is exist' )
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username ,
                password=password,email=email)
                user.set_password(password)
                user.save()
                print("Success")
                return redirect('login_user')
        else:
            messages.info(request, 'Both password are not mathching')
            return redirect(signup) 
   
        print("no post method") 
        return render(request,'signup.html')
def login_user(requst):
    if requst.method== 'POST':
        username =requst.POST['username']
        password=requst.POST['password']
        user= User.authenticate(username=username, password=password)    
        if user is not None:
            login(requst.user)
            return redirect(home)
        else:
            messages.info(requst,'user not exist')
            print('user not exist')
            return redirect(login_user)
    return render(requst,'login.html')
def user_logout(request):
    logout(request)
    return redirect(user_logout)   
def   add(request):
    form=bookform()
    if(request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
        return render(request,'add.html',{'form': form})
def booklist(request):
    b=Book.objects.all()
    return render (request,'view.html',{'b':b})    
def edit_book(request,p):
    b=Book.objects.get(pk=p)
    form=bookform(instance=b)
    if(request.method == "POST"):
        form=bookform(request.POST,request.FILES,instance=b)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add.html',{'form':form})
def view_book(requst,p):
    b=Book.objects.get(pk=p)
    return render(requst,'book.html',{'b':b})
def delete_book(request,p):
    b=Book.objects.get(pk=p)
    b.delete()
    return booklist(request)

