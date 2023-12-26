from django.contrib import admin
from appUser.models import *


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user','title')
    search_fields = ('title', 'user_username')

