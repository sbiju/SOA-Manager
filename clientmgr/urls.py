# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

app_name = 'clientmgr'

from . import views

urlpatterns = [
    url(r'^$', views.ClientsView.as_view(), name='clients'),
    url(r'^(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='client_details'),
    
    # Clients
    url(r'^client/create/$', views.ClientCreate.as_view(), name='client_create'),
    url(r'^client/(?P<pk>\d+)/$', views.ClientUpdate.as_view(), name='client_update'),
    url(r'^client/(?P<pk>\d+)/delete/$', views.ClientDelete.as_view(), name='client_delete'),
    
    # Partners
    url(r'^partner/create/$', views.PartnerCreate.as_view(), name='partner_create'),
    url(r'^partner/(?P<pk>\d+)/$', views.PartnerUpdate.as_view(), name='partner_update'),
    url(r'^partner/(?P<pk>\d+)/delete/$', views.PartnerDelete.as_view(), name='partner_delete'),
    
    # Entities
    url(r'^entity/all/$', views.EntitiesView.as_view(), name='entities'),
    url(r'^entity/create/$', views.EntityCreate.as_view(), name='entity_create'),
    url(r'^entity/(?P<pk>\d+)/$', views.EntityUpdate.as_view(), name='entity_update'),
    url(r'^entity/(?P<pk>\d+)/delete/$', views.EntityDelete.as_view(), name='entity_delete'),
]
