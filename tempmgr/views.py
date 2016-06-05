from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView 

# Models
from .models import Template, Subtemplate, Formatting, FormattingDetail

# --- Templates --------------------------------------------------- #
class TemplatesView(generic.ListView):
	template_name = 'tempmgr/templates.html'
	context_object_name = 'templates'
	
	def get_queryset(self):
		return Template.objects.all()
		
class TemplateDetailView(generic.DetailView):
	model = Template
	template_name = 'tempmgr/template_create.html'
	
class TemplateCreate(CreateView):
	model = Template	
	fields = ['tempID', 'tempName', 'description', 'tempType', 'notes', 'udoxTempCombiner', 
		'udoxFormatSetter', 'udoxCleanUp', 'udoxDraftUpdater', 'udoxMain', 'wksClientData', 'wksTempData',
		'wksStratData'
	]
		
	def get_success_url(self):
		return urlresolvers.reverse("tempmgr:templates")
	
class TemplateUpdate(UpdateView):
	model = Template
	fields = ['tempID', 'tempName', 'description', 'tempType', 'notes', 'udoxTempCombiner', 
		'udoxFormatSetter', 'udoxCleanUp', 'udoxDraftUpdater', 'udoxMain', 'wksClientData', 'wksTempData',
		'wksStratData'
	]
	
class TemplateDelete(DeleteView):
	model = Template
	success_url = reverse_lazy('tempmgr:templates')

# --- Subtemplates --------------------------------------------------- #
class SubtemplatesView(generic.ListView):
	template_name = 'tempmgr/subtemplates.html'
	context_object_name = 'subtemplates'
	
	def get_queryset(self):
		return Subtemplate.objects.all()
		
class SubtemplateDetailView(generic.DetailView):
	model = Subtemplate
	template_name = 'tempmgr/subtemplate_create.html'
	
class SubtemplateCreate(CreateView):
	model = Subtemplate	
	fields = ['subTempID', 'parentTempID', 'tempType', 'isIncluded', 'HasPageBreak', 'subTempGdocID', 
		'subTempGdocLink', 'parentGdocID', 'parentGdocLink'
	]
	
class SubtemplateUpdate(UpdateView):
	model = Subtemplate
	fields = ['subTempID', 'parentTempID', 'tempType', 'isIncluded', 'HasPageBreak', 'subTempGdocID', 
		'subTempGdocLink', 'parentGdocID', 'parentGdocLink'
	]
	
class SubtemplateDelete(DeleteView):
	model = Subtemplate
	success_url = reverse_lazy('tempmgr:templates')
	
# --- Formatting ----------------------------------------------------- #
class FormattingsView(generic.ListView):
	template_name = 'tempmgr/formattings.html'
	context_object_name = 'formattings'
	
	def get_queryset(self):
		return Formatting.objects.all()
		
class FormattingDetailView(generic.DetailView):
	model = Formatting
	template_name = 'tempmgr/formatting_create.html'
	
class FormattingCreate(CreateView):
	model = Formatting	
	template_name = 'tempmgr/formatting_create.html'
	fields = ['styleID', 'styleName', 'description']
	
	def get_success_url(self):
		return urlresolvers.reverse("tempmgr:templates")
	
class FormattingUpdate(UpdateView):
	model = Formatting
	fields = ['styleID', 'styleName', 'description']
	
class FormattingDelete(DeleteView):
	model = Formatting
	success_url = reverse_lazy('tempmgr:formatting')
	
# --- FormattingDetails ----------------------------------------------------- #		
class FormattingDetailsView(generic.ListView):
	template_name = 'tempmgr/formattingdetails.html'
	context_object_name = 'formattingdetails'
	
	def get_queryset(self):
		return FormattingDetail.objects.all()
		
class FormattingDetailDetailView(generic.DetailView):
	model = FormattingDetail
	template_name = 'tempmgr/formattingdetails_create.html'
	
class FormattingDetailCreate(CreateView):
	model = FormattingDetail	
	fields = ['styleID', 
		'title_font', 'title_fontsize', 'title_forecolor', 'title_bold', 'title_italic', 'title_alignment', 
		'subtitle_font', 'subtitle_fontsize', 'subtitle_forecolor', 'subtitle_bold', 'subtitle_italic', 'subtitle_alignment', 
		'normal_font', 'normal_fontsize', 'normal_forecolor', 'normal_bold', 'normal_italic', 'normal_alignment',
		'h1_font', 'h1_fontsize', 'h1_forecolor', 'h1_bold', 'h1_italic', 'h1_alignment',
		'h2_font', 'h2_fontsize', 'h2_forecolor', 'h2_bold', 'h2_italic', 'h2_alignment',
		'h3_font', 'h3_fontsize', 'h3_forecolor', 'h3_bold', 'h3_italic', 'h3_alignment',
		'h4_font', 'h4_fontsize', 'h4_forecolor', 'h4_bold', 'h4_italic', 'h4_alignment',
		'h5_font', 'h5_fontsize', 'h5_forecolor', 'h5_bold', 'h5_italic', 'h5_alignment',
		'h6_font', 'h6_fontsize', 'h6_forecolor', 'h6_bold', 'h6_italic', 'h6_alignment',
		'normal_font', 'normal_fontsize', 'normal_forecolor', 'normal_bold', 'normal_italic', 'normal_alignment'
	]
	
class FormattingDetailUpdate(UpdateView):
	model = FormattingDetail
	fields = ['styleID', 
		'title_font', 'title_fontsize', 'title_forecolor', 'title_bold', 'title_italic', 'title_alignment', 
		'subtitle_font', 'subtitle_fontsize', 'subtitle_forecolor', 'subtitle_bold', 'subtitle_italic', 'subtitle_alignment', 
		'normal_font', 'normal_fontsize', 'normal_forecolor', 'normal_bold', 'normal_italic', 'normal_alignment',
		'h1_font', 'h1_fontsize', 'h1_forecolor', 'h1_bold', 'h1_italic', 'h1_alignment',
		'h2_font', 'h2_fontsize', 'h2_forecolor', 'h2_bold', 'h2_italic', 'h2_alignment',
		'h3_font', 'h3_fontsize', 'h3_forecolor', 'h3_bold', 'h3_italic', 'h3_alignment',
		'h4_font', 'h4_fontsize', 'h4_forecolor', 'h4_bold', 'h4_italic', 'h4_alignment',
		'h5_font', 'h5_fontsize', 'h5_forecolor', 'h5_bold', 'h5_italic', 'h5_alignment',
		'h6_font', 'h6_fontsize', 'h6_forecolor', 'h6_bold', 'h6_italic', 'h6_alignment',
		'normal_font', 'normal_fontsize', 'normal_forecolor', 'normal_bold', 'normal_italic', 'normal_alignment'
	]
	
class FormattingDetailDelete(DeleteView):
	model = FormattingDetail
	success_url = reverse_lazy('tempmgr:formattingdetails')