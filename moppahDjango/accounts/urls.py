# URLS DO MEU APP ACCOUNTS
from django.urls import (path, include, re_path)
from moppahDjango.core.views import (home, contact)
#from moppahDjango.core.views import contact
#from moppahDjango.accounts.views import 
#from moppahDjango.accounts.views import 
from moppahDjango.accounts.views import (edit, edit_password, password_reset, password_reset_confirm,dashboard,register)
from django.contrib.auth.views import (LoginView, LogoutView)
#from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(),
        {'template_name': 'accounts/login.html'}, name='login'),
    path('sair/', LogoutView.as_view(),
        {'next_page': 'home'}, name='logout'),
    path('cadastre-se/', register, name='register'),
    path('nova_senha/', password_reset, name='password_reset'),
    re_path(r'^confirma_nova_senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password'),
]