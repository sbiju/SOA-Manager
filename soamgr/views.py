from django.db.models import Q
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin

from .models import Soa, SoaType, Strategy, Goal


class Adviser_BaseView(LoginRequiredMixin, TemplateView):
    """
    Handles post for Order SOA
    """
    
    template_name = "soamgr/adviser_base.html"

    def get_context_data(self, **kwargs):
        context = super(Adviser_BaseView, self).get_context_data(**kwargs)
        context['oas_saved'] = Soa.objects.filter(is_submitted=False, is_claimed=False, is_completed=False) # ~Q(status='1'), 
        context['oas_inprogress'] = Soa.objects.filter(is_submitted=True, is_claimed=False, is_completed=False) # ~Q(status='2'), 
        context['soas_inprogress'] = Soa.objects.filter(is_submitted=True, is_claimed=True, is_completed=False) # ~Q(status='3')
        context['soas_forreview'] = Soa.objects.filter(is_submitted=True, is_claimed=True, is_completed=True) # ~Q(status='4'), 

        return context

class Oa_CreateView(LoginRequiredMixin, CreateView):
    """
    Handles Create view for Ordering SOA
    """    
    template_name = "soamgr/oa_create.html"
    fields = ['client_name', 'attachment_file', 'is_submitted', 'date_created', 'date_due', ]
    model = Soa
    
    def get_success_url(self):
        return urlresolvers.reverse("soamgr:adviser_base")
        
    
class Oa_UpdateView(LoginRequiredMixin, UpdateView):

    template_name = "soamgr/oa_update.html"
    fields = ['client_name', 'attachment_file', 'is_submitted', 'date_created', 'date_due',]

    model = Soa

    def get_context_data(self, **kwargs):
        context = super(Oa_UpdateView, self).get_context_data(**kwargs)
        context['id_updated'] = self.kwargs.get('pk')
        
        return context

    def get_success_url(self):
        return urlresolvers.reverse("soamgr:adviser_base")

    def get_object(self):
        # Only get the order record making the request
        return Soa.objects.get(id=self.kwargs.get('pk'))

    def post(self, request, **kwargs): 
        if 'is_submitted' in request.POST:
            is_submitted = True
            status = '2'
        else:
            is_submitted = False
            status = '1'
        
        current_oa = Soa.objects.get(id=self.kwargs.get('pk'))
        current_oa.is_submitted = is_submitted
        current_oa.is_claimed = False
        current_oa.is_completed = False
        current_oa.status = status
        current_oa.save()
        
        return HttpResponseRedirect(urlresolvers.reverse("soamgr:adviser_base"))
        
class Adviser_ReviewSoa(LoginRequiredMixin, UpdateView):
    """
    Handles view for Review order agreement
    """

    template_name = "soamgr/review_soa.html"
    fields = ['client_name', 'attachment_file', 'is_submitted', 'date_created', 'date_due',]
    model = Soa

    def get_context_data(self, **kwargs):
        context = super(Adviser_ReviewSoa, self).get_context_data(**kwargs)
        context['soa'] = get_object_or_404(Soa, pk=self.kwargs.get('pk'))            
        context['soa_types'] = SoaType.objects.all()
        
        return context

    def post(self, request, **kwargs):
        soa_type = request.POST.get('soa-type')
        
        current_soa = Soa.objects.get(id=self.kwargs.get('pk'))       
        soa_types = SoaType.objects.get(id=soa_type)
        
        print soa_types
        current_soa.comments = request.POST.get('comments')
        current_soa.soa_type = SoaType.objects.get(id=soa_type)
        
        if 'is-submit' in request.POST:
            current_soa.is_submitted = True
        else:
            current_soa.is_submitted = False       
            
        current_soa.save()
        return HttpResponseRedirect(urlresolvers.reverse("soamgr:adviser_base"))


class QppAdmin_Base(LoginRequiredMixin, TemplateView):
    """
    Handles view for QPP Admin
    """

    template_name = "soamgr/qppadmin_base.html"

    def get_context_data(self, **kwargs):
        context = super(QppAdmin_Base, self).get_context_data(**kwargs)
        context['oas_received'] = Soa.objects.filter(
            is_submitted=True, is_approved=False, is_claimed=False, is_completed=False
        )
        context['oas_inprogress'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=False, is_completed=False
        )
        context['soas_claimed'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=True, is_completed=False, progress__lte=0
        )
        context['soas_inprogress'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=True, is_completed=False, progress__gt=0, progress__lt=100
        )
        context['soas_forreview'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=False, is_completed=True, progress__gte=100
        )

        return context
        

class QppAdmin_SoaSettings(LoginRequiredMixin, TemplateView):
    """
    Handles view for QPP Admin
    """

    template_name = "soamgr/soasettings.html"

    def get_context_data(self, **kwargs):
        context = super(QppAdmin_SoaSettings, self).get_context_data(**kwargs)
        context['soatypes'] = SoaType.objects.all()
        context['strategies'] = Strategy.objects.all()
        context['goals'] = Goal.objects.filter()

        return context

class QppAdmin_SoaTypeCreateView(LoginRequiredMixin, CreateView):
    """
    Handles Create view for Ordering SOA
    """    
    template_name = "soamgr/soatype_update.html"
    model = SoaType
    fields = ['type_name', 'description', 'guaranteed_time', 'paraplanner_time', 'cost', 'paraplanner_cost',]
    
    def get_success_url(self):
        return urlresolvers.reverse("soamgr:qppadmin_soasettings")
        
    
class QppAdmin_SoaTypeUpdateView(LoginRequiredMixin, UpdateView):

    template_name = "soamgr/oa_update.html"
    fields = ['client_name', 'attachment_file', 'is_submitted', 'date_created', 'date_due',]

    model = SoaType

    def get_context_data(self, **kwargs):
        context = super(QppAdmin_SoaTypeUpdateView, self).get_context_data(**kwargs)
        context['id_updated'] = self.kwargs.get('pk')
        
        return context

    def get_success_url(self):
        return urlresolvers.reverse("soamgr:adviser_base")

    def get_object(self):
        # Only get the order record making the request
        return Soa.objects.get(id=self.kwargs.get('pk'))

    def post(self, request, **kwargs): 
        if 'is_submit' in request.POST:
            is_submit = True
            status = '2'
        else:
            is_submit = False
            status = '1'
        
        current_soa = Soa.objects.get(id=self.kwargs.get('pk'))
        current_soa.is_submitted = is_submit
        current_soa.is_claimed = False
        current_soa.is_completed = False
        current_soa.status = status
        current_soa.save()
        
        return HttpResponseRedirect(urlresolvers.reverse("soamgr:adviser_base"))

class QppAdmin_OaApproval(LoginRequiredMixin, TemplateView):
    """
    Handles view for QPP Admin approval
    """
    
    template_name = "soamgr/oa_approval.html"

    def get_context_data(self, **kwargs):
        context = super(QppAdmin_OaApproval, self).get_context_data(**kwargs)
        context['current_oa'] = Soa.objects.get(id=kwargs.get('pk'))

        return context

    def post(self, request, **kwargs):
        current_oa = request.POST.get('oa-id')
        approval_choice = request.POST.get('approval-choice')

        current_oa = Soa.objects.get(id=current_oa)
        if approval_choice == '1':
            current_oa.is_approved = True

        current_oa.approval_choice = approval_choice
        current_oa.save()

        return HttpResponseRedirect(urlresolvers.reverse("soamgr:qppadmin_base"))


class Paraplanner_BaseView(LoginRequiredMixin, TemplateView):
    """
    Handles view for Paraplanner dashboard
    """
    
    template_name = "soamgr/paraplanner_base.html"

    def get_context_data(self, **kwargs):
        context = super(Paraplanner_BaseView, self).get_context_data(**kwargs)
        context['jobs_available'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=False, is_completed=False, paraplanner_approver__isnull=True
        )
        context['jobs_inprogress'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=True, is_completed=False, paraplanner_approver__isnull=False
        )
        context['jobs_completed'] = Soa.objects.filter(
            is_submitted=True, is_approved=True, is_claimed=True, is_completed=True, paraplanner_approver__isnull=False
        )

        return context


class Paraplanner_ClaimJob(LoginRequiredMixin, TemplateView):
    """
    Handles view for Paraplanner Claim Job
    """

    template_name = "soamgr/claim_job.html"

    def get_context_data(self, **kwargs):
        context = super(Paraplanner_ClaimJob, self).get_context_data(**kwargs)
        context['current_id'] = self.kwargs.get('pk')
        context['current_soa'] = Soa.objects.filter(id=self.kwargs.get('pk'))

        return context

    def post(self, request, **kwargs):
        soa_toclaim = Soa.objects.get(id=kwargs.get('pk'))
        if 'is-claimed' in request.POST:
            soa_toclaim.paraplanner_approver = self.request.user
            soa_toclaim.is_claimed = True
            
        soa_toclaim.save()

        return HttpResponseRedirect(urlresolvers.reverse("soamgr:paraplanner_base"))