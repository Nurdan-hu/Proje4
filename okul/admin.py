from django.contrib import admin
from .models import Kadro

class OgretmenAdmin(admin.ModelAdmin):
  list_display = ("AdiSoyadi" , "Bransi" , "Sinifi" , "Aciklama")

admin.site.register(Kadro , OgretmenAdmin)
