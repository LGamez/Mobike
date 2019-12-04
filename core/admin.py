from django.contrib import admin
from .models import Portafolio

# Register your models here.
class PortafolioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_crea','fecha_publ')


admin.site.register(Portafolio, PortafolioAdmin)

