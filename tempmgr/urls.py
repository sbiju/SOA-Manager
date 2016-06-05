# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

app_name = 'tempmgr'

from . import views

urlpatterns = [
    url(r'^$', views.TemplatesView.as_view(), name='templates'),
    url(r'^(?P<pk>\d+)/$', views.TemplateDetailView.as_view(), name='template_details'),
    
    # Templates
    url(r'^template/create/$', views.TemplateCreate.as_view(), name='template_create'),
    url(r'^template/(?P<pk>\d+)/$', views.TemplateUpdate.as_view(), name='template_update'),
    url(r'^template/(?P<pk>\d+)/delete/$', views.TemplateDelete.as_view(), name='template_delete'),
    
    # Subtemplates
    url(r'^subtemplate/all/$', views.SubtemplatesView.as_view(), name='subtemplates'),
    url(r'^subtemplate/create/$', views.SubtemplateCreate.as_view(), name='subtemplate_create'),
    url(r'^subtemplate/(?P<pk>\d+)/$', views.SubtemplateUpdate.as_view(), name='subtemplate_update'),
    url(r'^subtemplate/(?P<pk>\d+)/delete/$', views.SubtemplateDelete.as_view(), name='subtemplate_delete'),
    
    # Formatting
    url(r'^formatting/all/$', views.FormattingsView.as_view(), name='formattings'),
    url(r'^formatting/create/$', views.FormattingCreate.as_view(), name='formatting_create'),
    url(r'^formatting/(?P<pk>\d+)/$', views.FormattingUpdate.as_view(), name='formatting_update'),
    url(r'^formatting/(?P<pk>\d+)/delete/$', views.FormattingDelete.as_view(), name='formatting_delete'),
    
    # FormattingDetails
    url(r'^formattingdetail/all/$', views.FormattingDetailsView.as_view(), name='formattingdetails'),
    url(r'^formattingdetail/create/$', views.FormattingDetailCreate.as_view(), name='formattingdetail_create'),
    url(r'^formattingdetail/(?P<pk>\d+)/$', views.FormattingDetailUpdate.as_view(), name='formattingdetail_update'),
    url(r'^formattingdetail/(?P<pk>\d+)/delete/$', views.FormattingDetailDelete.as_view(), name='formattingdetail_delete'),
]
