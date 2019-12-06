from django.contrib import admin
from .models import Adoptante
from .models import Cliente
from .models import Perros , Estado

admin.site.register(Adoptante)
admin.site.register(Cliente)
admin.site.register(Perros)
