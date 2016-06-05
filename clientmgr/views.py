from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView 

# Models
from .models import Client, Partner, Entity

# --- Clients --------------------------------------------------- #
class ClientsView(generic.ListView):
	template_name = 'clientmgr/clients.html'
	context_object_name = 'clients'
	
	def get_queryset(self):
		return Client.objects.all()
		
class ClientDetailView(generic.DetailView):
	model = Client
	template_name = 'clientmgr/client_create.html'
	
class ClientCreate(CreateView):
	model = Client
	fields = ['clientID', 'xplanID', 'title', 'lastName', 'middleName', 'firstName', 
		'secondName', 'preferredName', 'fullName', 'completeName', 'photo', 'email',
		'mobilePhone', 'homePhone', 'addressLine1', 'addressLine2', 'addressLine3'
	]
	
class ClientUpdate(UpdateView):
	model = Client
	fields = ['clientID', 'xplanID', 'title', 'lastName', 'middleName', 'firstName', 
		'secondName', 'preferredName', 'fullName', 'completeName', 'photo', 'email',
		'mobilePhone', 'homePhone', 'addressLine1', 'addressLine2', 'addressLine3'
	]
	
class ClientDelete(DeleteView):
	model = Client
	success_url = reverse_lazy('clientmgr:clients')

# --- Partners --------------------------------------------------- #
class PartnerDetailView(generic.DetailView):
	model = Partner
	template_name = 'clientmgr/partner_create.html'
	
class PartnerCreate(CreateView):
	model = Partner
	fields = ['partnerID', 'xplanID', 'title', 'lastName', 'middleName', 'firstName', 
		'secondName', 'preferredName', 'fullName', 'completeName', 'photo', 'email',
		'mobilePhone', 'homePhone', 'addressLine1', 'addressLine2', 'addressLine3'
	]
	
class PartnerUpdate(UpdateView):
	model = Partner
	fields = ['partnerID', 'xplanID', 'title', 'lastName', 'middleName', 'firstName', 
		'secondName', 'preferredName', 'fullName', 'completeName', 'photo', 'email',
		'mobilePhone', 'homePhone', 'addressLine1', 'addressLine2', 'addressLine3'
	]
	
class PartnerDelete(DeleteView):
	model = Partner
	success_url = reverse_lazy('clientmgr:clients')
	
# --- Entities --------------------------------------------------- #
class EntitiesView(generic.ListView):
	template_name = 'clientmgr/entities.html'
	context_object_name = 'entities'
	
	def get_queryset(self):
		return Entity.objects.all()
		
class EntityDetailView(generic.DetailView):
	model = Entity
	template_name = 'clientmgr/entity_create.html'
	
class EntityCreate(CreateView):
	model = Entity
	fields = ['entityID', 'xplanID', 'name', 'description', 'entType', 'incomes', 
		'expenses', 'investments', 'assets', 'debts', 'netFinancial', 'defensiveAssets',
		'growthAssets', 'riskProfile', 'assessment', 'about'
	]
	
class EntityUpdate(UpdateView):
	model = Entity
	fields = ['entityID', 'xplanID', 'name', 'description', 'entType', 'incomes', 
		'expenses', 'investments', 'assets', 'debts', 'netFinancial', 'defensiveAssets',
		'growthAssets', 'riskProfile', 'assessment', 'about'
	]
	
class EntityDelete(DeleteView):
	model = Entity
	success_url = reverse_lazy('clientmgr:entities')
	
