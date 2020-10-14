# URLS DO MEU PROJETO EM CORE
from django.urls import path
from moppahDjango.core.views import (home, contact)

urlpatterns = [
    path('',home, name='home'),
    path('contato/',contact, name='contact'),
]