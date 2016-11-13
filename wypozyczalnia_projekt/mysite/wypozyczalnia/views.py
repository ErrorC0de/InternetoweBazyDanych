from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

# Create your views here.


class AboutView(TemplateView):
    template_name = "wypozyczalnia/about.html"


class HomeView(TemplateView):
 	template_name = "wypozyczalnia/home.html"

