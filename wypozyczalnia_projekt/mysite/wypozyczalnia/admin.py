from django.contrib import admin

# Register your models here.

from .models import Producent, Kategoria, Sprzet, PunktSerwisowy, Egzemplarz, Koszyk, Rezerwacja
from django.contrib.auth.models import User



admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Sprzet)
admin.site.register(PunktSerwisowy)
admin.site.register(Egzemplarz)
admin.site.register(Koszyk)
admin.site.register(Rezerwacja)