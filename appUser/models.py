from django.db import models
from django.contrib.auth.models import User # User modelii çagırmamıza yarar


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Profil Adı"), max_length=50)
    image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=None)
    
    def __str__(self):
        return self.title + " " + self.user.username
    
    