from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.views.generic import FormView, ListView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from wypozyczalnia.models import Sprzet, Kategoria
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