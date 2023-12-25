from django.shortcuts import render

# Create your views here.

def indexPage(request):
    context = {}
    return render(request, "index.html",context)

def browsePage(request):
    context = {}
    return render(request,"browse.html", context)

def browse_indexPage(request):
    context = {}
    return render(request, "browse-index.html", context)