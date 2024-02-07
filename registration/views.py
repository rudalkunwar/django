from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('This is about page')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def blogs(request):
    return render(request,'blogs.html')

def signup(request):
    error_messsage = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
    if password!=cpassword:
        error_messsage="Password doesnot match"
    else:
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    
    return render(request,'register.html',{"error_messsage":error_messsage})