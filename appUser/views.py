from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

def profilPage(request):
    context = {}
    return render(request,"profil.html", context)


def hesapPage(request):
    context = {}
    return render(request, "hesap.html", context)
def videoPage(request):
    context ={}
    return render(request,"video.html", context)



def loginPage(request):
    context = {}
    return render(request,"user/login.html", context)

def registerPage(request):
    context = {}
    return render(request,"user/register.html", context)
