from django.shortcuts import render,HttpResponse
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
# def signup(request):
#     if(request.method == 'POST'):