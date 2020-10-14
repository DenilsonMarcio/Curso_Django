# URLS DO MEU PROJETO EM CORE
from django.urls import path
from moppahDjango.core.views import home
from moppahDjango.core.views import contact


urlpatterns = [
    path('',home, name='home'),
    path('contato/',contact, name='contact'),
]