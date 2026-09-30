from django.contrib import admin
from shop.models import Fruta
# Register your models here.
class FrutaAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','oferta']
admin.site.register(Fruta,FrutaAdmin)

