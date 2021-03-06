from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import sites
from . import forms
from wypozyczalnia.views import SprzetListView, SprzetDetailView, KoszykListView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
url(r'^$', views.HomeView.as_view(), name='home'),
url(r'^projekt/$', TemplateView.as_view(template_name="wypozyczalnia/about.html")),
url(r'^katalog/$', SprzetListView.as_view(template_name= "wypozyczalnia/katalog.html"), name='sprzet-list'),
url(r'^katalog/sprzet/(?P<post_id>\d+)/$', SprzetDetailView.as_view(template_name="wypozyczalnia/sprzet_szczegol.html")),
#url(r'^login$', TemplateView.as_view(template_name= "wypozyczalnia/login.html")),
url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
url(r'^logout/$', auth_views.logout, {'redirect_field_name': 'next'}, name='logout'),
url(r'^do_koszyka/(?P<post_id>\d+)/$', views.do_koszyka),
url(r'^koszyk/$', KoszykListView.as_view(template_name= "wypozyczalnia/koszyk.html"), name='koszyk-list'),
 url(r'^', include('registration.backends.simple.urls')),


#url(r'^items/$', views.ItemsView.as_view(), name='items'),
#url(r'^items/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
#url(r'^basket/(?P<pk>[0-9]+)$', views.BasketView.as_view(), name='basket'),
#url(r'^login$', views.LoginView.as_view(), name='login'),
]