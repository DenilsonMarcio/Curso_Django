# URLS DO MEU PROJETO EM CORE
from django.urls import path
from moppahDjango.core.views import (home, contact)

#app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('contato/',contact, name='contact'),
]