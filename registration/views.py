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

def loginpage(request):
    return render(request,'login.html')

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
        login(request,myuser)
        return redirect('blogs',user=username)
    
    return render(request,'register.html',{"error_messsage":error_messsage})

def signin(request):
    error_messsage = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('blogs',user=username)
        else:
            error_messsage="Username or Eamil doesnot match!!"
    
    return render(request,'login.html',{"error_messsage":error_messsage})

@login_required(login_url='login')
def blogs(request, user=None):
    return render(request, 'blogs.html')

def signout(request):
    logout(request)
    return redirect('index')
