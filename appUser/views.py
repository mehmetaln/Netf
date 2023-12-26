from django.shortcuts import render, redirect #redirect yönlendirme işlemleri için kullanılır
from django.contrib.auth import login, logout, authenticate #  giriş yap çıkış yap ve kullanııc kontrol işlemleri için
from django.contrib.auth.models import User # user modelini çekmemize yarar
from django.contrib import messages # messages modeülünü kullanmamıza yarar

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
            request.session.set_expiry(1209600) # beni hatırla check-box kaç dakika hatırlı kalacağını verir bize
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
    if request.method == "POST":
        lname =request.POST.get("fname")  
        fname = request.POST.get("lname")
        email =request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        check_site = request.POST.get("check-site")
        check_kvkk = request.POST.get("check-kvkk")
# Önce Tüm degişkenlerimi getirdim şekilde

        if fname and lname and email and password1 and password2 and check_site and check_kvkk: # tüm alanların doldurulup doldurulmadığını kontrol ediyoruz
            if password1 == password2: # parolalar uyuşuyor mu diye kontrol ediyoruz
                if not User.objects.filter(username = username).exists(): # benim datalarımın arasında böyle bir kullanıcı varmı diye kontrol diyoruz
                    if not User.objects.filter(email = email).exists(): # aynı şekilde mail varmı diye
                        user = User.objects.create_user(first_name=fname, last_name = lname, username=username, email=email, password=password1) # tüm değişkenleri yeni kullanıcıcya kaydediyoruz
                        user.save() # kayıt tamamlanıyor
                        messages.success(request,"Kaydınız başarılı bir şekilde oluşturuldu") # mesaj gönderiyoruz
                        return redirect("loginPage") # ilişkili sayfaya
                    else:
                        messages.error(request,"Bu email zaten kullanılmakta")
                else:
                    messages.error(request,"Bu kullanıcı adı zaten kullanılmakta")
            else:
                messages.error(request,"Parolalar uyuşmuyor")
        else:
            messages.error(request,"Lütfen tüm boşlukları doldurunuz") 
   
   
    context = {}
    return render(request,"user/register.html", context)
