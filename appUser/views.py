from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

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
    
    if request.method == "POST":
        username = request.POST.get("username")
        password =request.POST.get("password")
        remember = request.POST.get("rememberme") 
        
        if remember:
            request.session.set_expiry(1209600)
        else:
            request.session.set_expiry(0)
            
        
        user =authenticate(username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, "Girişiniz Yapıldı")
            return redirect('profilPage')
        else:
            messages.error(request,"Kullanıcı adınız veya Şifreniz yanlış")
            return redirect("loginPage")
            
    
    
    context = {}
    return render(request,"user/login.html", context)

def registerPage(request):
    context = {}
    return render(request,"user/register.html", context)
