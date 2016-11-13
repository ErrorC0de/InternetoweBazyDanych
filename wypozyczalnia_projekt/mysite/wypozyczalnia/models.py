from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producent(models.Model):
	nazwa = models.CharField(max_length=40)
	adres = models.CharField(max_length=40)
	telefon = models.CharField(max_length=10)

class Kategoria(models.Model):
	nazwa = models.CharField(max_length=40)

class Sprzet(models.Model):
	nazwa = models.CharField(max_length=40)
	producent = models.ForeignKey(Producent, on_delete=models.CASCADE)
	kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)

class PunktSerwisowy(models.Model):
	nazwa = models.CharField(max_length=40)
	adres = models.CharField(max_length=40)
	telefon = models.CharField(max_length=40)

class Egzemplarz(models.Model):
	sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
	punkt_serwisowy = models.ForeignKey(PunktSerwisowy, on_delete=models.CASCADE)
	data_ostatniego_przegladu = models.DateTimeField()
	wycofany = models.BooleanField(default=False)
	data_zakupu = models.DateTimeField()

class Koszyk(models.Model):
	klient = models.ForeignKey(User, on_delete=models.CASCADE)
	egzemplarz = models.ForeignKey(Egzemplarz, on_delete=models.CASCADE)
	sztuki = models.IntegerField(default=0)
	rezerwacja_od = models.DateTimeField()
	rezerwacja_do = models.DateTimeField()
	ilosc_godzin = models.IntegerField(default=0)

class Rezerwacja(models.Model):
	klient = models.ForeignKey(User, on_delete=models.CASCADE)
	egzemplarz = models.ForeignKey(Egzemplarz, on_delete=models.CASCADE)
	sztuki = models.IntegerField(default=0)
	rezerwacja_od = models.DateTimeField()
	rezerwacja_do = models.DateTimeField()
	ilosc_godzin = models.IntegerField(default=0)
	zrealizowano = models.BooleanField(default=False)

	