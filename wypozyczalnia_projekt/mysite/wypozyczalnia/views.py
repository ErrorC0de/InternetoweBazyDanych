from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.views.generic import FormView, ListView, TemplateView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
from wypozyczalnia.models import Sprzet, Kategoria, Egzemplarz
from wypozyczalnia.forms import IloscForm
from django import template
# Create your views here.


class AboutView(TemplateView):
    template_name = "wypozyczalnia/about.html"


class HomeView(TemplateView):
 	template_name = "wypozyczalnia/home.html"

class SprzetListView(ListView):

    model = Kategoria

    def get_context_data(self, **kwargs):
        context = super(SprzetListView, self).get_context_data(**kwargs)
        context['sprzet_list'] = Sprzet.objects.all()

        return context


class SprzetDetailView(DetailView):
	model = Sprzet
	pk_url_kwarg = "post_id"

	def get_context_data(self, **kwargs):
		context = super(SprzetDetailView, self).get_context_data(**kwargs)

		context['loop_times'] = range(1, Egzemplarz.objects.filter(sprzet__pk=self.kwargs['post_id'], wypozyczono=False).count()+1)
		context['sztuk'] = Egzemplarz.objects.filter(sprzet__pk=self.kwargs['post_id'], wypozyczono=False).count()
		return context



	#def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
	#	form.send_email()
	#	return super(ContactView, self).form_valid(form)


def do_koszyka(request, post_id):
	print('gello')
	sprzet = get_object_or_404(Sprzet, pk=post_id)
	set_list = sprzet.egzemplarz_set.filter(wypozyczono=False)[:int(request.POST.get('quantity', 0))]
	for egzemplarz in set_list:
		print(egzemplarz.id)
		egzemplarz.wypozyczono = True
		egzemplarz.wypozyczony_przez = request.user
		egzemplarz.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
	return HttpResponseRedirect('/katalog')

class KoszykListView(ListView):
	model = Egzemplarz
	def get_context_data(self, **kwargs):
		context = super(KoszykListView, self).get_context_data(**kwargs)
		context['egzemplarz_list'] = Egzemplarz.objects.filter(wypozyczony_przez = self.request.user)
		return context