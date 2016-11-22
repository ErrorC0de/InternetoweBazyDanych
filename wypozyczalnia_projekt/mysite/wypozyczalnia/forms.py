from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class IloscForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def send_email(self):
		pass