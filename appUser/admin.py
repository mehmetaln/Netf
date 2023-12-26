from django.contrib import admin
from appUser.models import *


@admin.register()
class Admin(Profil):
    '''Admin View for '''

    list_display = ('user','title')
    search_fields = ('title', 'user_username')

