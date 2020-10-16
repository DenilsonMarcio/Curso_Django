# URLS DO MEU PROJETO EM COURSE
from django.urls import path, re_path
from moppahDjango.courses.views import (courses, details, enrollment, announcements, undo_enrollment,show_announcement, lessons, lesson, material)

app_name = 'courses'

urlpatterns = [
    path('',courses, name='index'),
    #re_path(r'(?P<pk>\d+)/$',details, name='details'), #Adicionar o import re_re_path
    re_path(r'^(?P<slug>[\w_-]+)/$',details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/$',announcements, name='announcements'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$',show_announcement, name='show_announcement'),
    re_path(r'^(?P<slug>[\w_-]+)/inscricao/$',enrollment, name='enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$',undo_enrollment, name='undo_enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/$',lessons, name='lessons'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$',lesson, name='lesson'),
    re_path(r'^(?P<slug>[\w_-]+)/materias/(?P<pk>\d+)/$',material, name='material')
]

