from django.conf.urls import url
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'wypozyczalnia'
urlpatterns = [
url(r'^$', views.HomeView.as_view(), name='home'),
url(r'^projekt', views.AboutView.as_view()),
url(r'^login$', TemplateView.as_view(template_name= "wypozyczalnia/login.html")),
#url(r'^items/$', views.ItemsView.as_view(), name='items'),
#url(r'^items/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
#url(r'^basket/(?P<pk>[0-9]+)$', views.BasketView.as_view(), name='basket'),
#url(r'^login$', views.LoginView.as_view(), name='login'),
]