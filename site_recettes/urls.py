__author__ = 'Joaquim Ribeiro Esteves & Benjamin Bouret'


from django.conf.urls import patterns, url
from .views import Index

urlpatterns = patterns('',
                       url(r'^$', Index, name='index'),
                       )