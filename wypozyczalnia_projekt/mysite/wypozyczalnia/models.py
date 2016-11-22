from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producent(models.Model):
	nazwa = models.CharField(max_length=40)
	adres = models.CharField(max_length=40)
	telefon = models.CharField(max_length=10)

	def __str__(self):
		return str(self.nazwa)

class Kategoria(models.Model):
	nazwa = models.CharField(max_length=40)

	def __str__(self):
		return str(self.nazwa)

class Sprzet(models.Model):
	nazwa = models.CharField(max_length=40)
	producent = models.ForeignKey(Producent, on_delete=models.CASCADE)
	kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
	opis = models.CharField(max_length=255)
	zdjecie_link = models.CharField(max_length=255)
	def __str__(self):
		return str(self.nazwa)

class PunktSerwisowy(models.Model):
	nazwa = models.CharField(max_length=40)
	adres = models.CharField(max_length=40)
	telefon = models.CharField(max_length=40)

	def __str__(self):
		return str(self.nazwa)

class Egzemplarz(models.Model):
	sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
	punkt_serwisowy = models.ForeignKey(PunktSerwisowy, on_delete=models.CASCADE)
	data_ostatniego_przegladu = models.DateTimeField()
	wypozyczono = models.BooleanField(default=False)
	wycofany = models.BooleanField(default=False)
	data_zakupu = models.DateTimeField()
	wypozyczony_przez = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null=True)
	def get_niewypozyczone_ilosc(self, sprzet_fk):
		print('nowitam')
		return self.egzemplarz_set.get(wypozyczono=False, sprzet = sprzet_fk)

	def __str__(self):
		return str(self.sprzet) + "\n egzemplarz:" +str(self.id)

class Koszyk(models.Model):
	klient = models.ForeignKey(User, on_delete=models.CASCADE)
	egzemplarz = models.ForeignKey(Egzemplarz, on_delete=models.CASCADE)
	sztuki = models.IntegerField(default=0)
	rezerwacja_od = models.DateTimeField()
	rezerwacja_do = models.DateTimeField()
	ilosc_godzin = models.IntegerField(default=0)

	def __str__(self):
		return str(self.klient)

class Rezerwacja(models.Model):
	klient = models.ForeignKey(User, on_delete=models.CASCADE)
	egzemplarz = models.ForeignKey(Egzemplarz, on_delete=models.CASCADE)
	sztuki = models.IntegerField(default=0)
	rezerwacja_od = models.DateTimeField()
	rezerwacja_do = models.DateTimeField()
	ilosc_godzin = models.IntegerField(default=0)
	zrealizowano = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)
