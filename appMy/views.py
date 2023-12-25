from django.shortcuts import render

# Create your views here.

def indexPage(request):
    context = {}
    return render(request, "index.html",context)

def profilPage(request):
    context = {}
    return render(request,"profil.html", context)

def browsePage(request):
    context = {}
    return render(request, "browse.html", context)


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
