from django.shortcuts import render

# Create your views here.

def hesapPage(request):
    context = {}
    return render(request, "hesap.html", context)


def loginPage(request):
    context = {}
    return render(request,"login.html", context)

def videoPage(request):
    context ={}
    return render(request,"video.html", context)