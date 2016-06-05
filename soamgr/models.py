from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
#from django_countries import CountryField
from django.contrib.postgres.fields import JSONField # For Goals and Strategies

from model_utils.models import TimeStampedModel

from project_soa.users.models import User

optional = {
    "null": True,
    "blank": True,
}


@python_2_unicode_compatible
class SoaType(models.Model):
    """
    Model for SOA types
    """                        
    type_name               = models.CharField(_('Type Name'), max_length=254)
    description             = models.CharField(_('Description'), max_length=254, **optional)
    guaranteed_time         = models.SmallIntegerField(default=72)
    paraplanner_time        = models.SmallIntegerField(default=24)
    cost                    = models.DecimalField(default=200, decimal_places=2, max_digits=6)
    paraplanner_cost        = models.DecimalField(default=100, decimal_places=2, max_digits=6)
    
    class Meta(object):
        verbose_name = _('Soa Type')
        verbose_name_plural = _('Soa Types')
    
    def __str__(self):
        return "{} - ${}".format(self.type_name, self.cost)
        

@python_2_unicode_compatible
class Strategy(models.Model):
    """
    Model for SOA Strategies
    """                       
    
    strat_name              = models.CharField(_('Strategy Name'), max_length=254)
    description             = models.CharField(_('Description'), max_length=254, **optional)
    parent                  = models.CharField(_('Parent Strategy'), max_length=254)
    sort                    = models.SmallIntegerField()
    
    class Meta(object):
        verbose_name = _('Soa Strategy')
        verbose_name_plural = _('Soa Strategies')
    
    def __str__(self):
        return "{} - {}".format(self.id, self.strat_name)
        
        
@python_2_unicode_compatible
class Goal(models.Model):
    """
    Model for SOA Strategies
    """                      
    
    goal_name               = models.CharField(_('Goal Name'), max_length=254)
    description             = models.CharField(_('Description'), max_length=254, **optional)
    parent                  = models.CharField(_('Parent Goal'), max_length=254)
    sort                    = models.SmallIntegerField()
    
    class Meta(object):
        verbose_name = _('Client Objective')
        verbose_name_plural = _('Client Objectives')
    
    def __str__(self):
        return "{} - {}".format(self.id, self.goal_name)
        
        
@python_2_unicode_compatible
class Progress(models.Model):
    """
    Model for Soa Progress - intended for paraplanner's progress in creating SOA.
    """                      
    
    prog_name               = models.CharField(_('Progress Name'), max_length=254)
    description             = models.CharField(_('Description'), max_length=254, **optional)
    question                = models.CharField(_('Question'), max_length=254, **optional)
    parent                  = models.CharField(_('Parent Item'), max_length=254)
    task_percent            = models.SmallIntegerField(default=10)
    sort                    = models.SmallIntegerField()
    
    class Meta(object):
        verbose_name = _('Task Progress')
        verbose_name_plural = _('Task Progress Items')
    
    def __str__(self):
        return "{} - {}".format(self.id, self.prog_name)
        
        
@python_2_unicode_compatible
class EvalItem(models.Model):
    """
    Model for Evaluation Items - intended for admin and adviser's way of evaluating SOA.
    """                      
    
    eval_name               = models.CharField(_('Progress Name'), max_length=254)
    description             = models.CharField(_('Description'), max_length=254, **optional)
    question                = models.CharField(_('Question'), max_length=254, **optional)
    parent                  = models.CharField(_('Parent Item'), max_length=254)
    sort                    = models.SmallIntegerField()
    
    class Meta(object):
        verbose_name = _('Evaluation Item')
        verbose_name_plural = _('Evaluation Items')
    
    def __str__(self):
        return "{} - ${}".format(self.id, self.eval_name)
        

@python_2_unicode_compatible
class Soa(TimeStampedModel):
    """
    Model for SOA
    """
    STATUS_CHOICES = (
        ('1', 'OA saved'),
        ('2', 'OA in-progress'),
        ('3', 'SOA in-progress'),
        ('4', 'SOA for review'),
        ('5', 'SOA finished'),
    )
    
    APPROVAL_CHOICES = (
        ('1', 'OA Approved'),
        ('2', 'SOA started'),
        ('3', 'SOA finished'),
        ('4', 'SOA reviewed'),
    )
    
    client_name             = models.CharField(_('Client Name'), max_length=254)
    attachment_file         = models.FileField(upload_to='order_soa')
    date_created            = models.DateField(**optional)
    date_due                = models.DateField(**optional)
    status                  = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    is_submitted            = models.BooleanField(_('Is submitted?'), default=False)
    is_claimed              = models.BooleanField(_('Is claimed?'), default=False)
    is_approved             = models.BooleanField(_('Is completed?'), default=False)
    is_completed            = models.BooleanField(_('Is completed?'), default=False)
    
    soa_type                = models.ForeignKey(SoaType, related_name="soa_type", **optional)
    paraplanner_approver    = models.ForeignKey(User, **optional)
    comments                = models.TextField(_('Comments'), **optional)
    approval_choice         = models.CharField(max_length=1, choices=APPROVAL_CHOICES, **optional)
    
    goals                   = JSONField(**optional)    # Json Format: {goal_id1: is_included, goal_id2: is_included, ...}
    strategies              = JSONField(**optional)    # Json Format: {strat_id1: is_included, strat_id2: is_included, ...}
    
      
    """
    progress_items field - to fetch the tasks completed by the paraplanner for the job.
    
        Json Format: {prog_id1: [
                        is_completed: yes/no,
                        by_who: paraplanner or could be the adviser,
                        when: date the task is completed
                    ],
                    prog_id2: [
                        is_completed: yes/no,
                        by_who: paraplanner, or could be the adviser
                        when: date the task is completed
                    ]
                    ...
                    }
    """
    progress_items          = JSONField(**optional)  
    
    """
    eval_items field - to fetch the evaluation ratings of this current soa.
    
        Json Format: {eval_id1: [
                        rating: 1-10,
                        rated_by: qpp admin or could be the adviser,
                        feedback: any feedback
                    ],
                    eval_id2: [
                        rating: 1-10,
                        rated_by: qpp admin or could be the adviser,
                        feedback: any feedback
                    ]
                    ...
                    }
    """
    eval_items              = JSONField(**optional)    
    
    
    progress                = models.SmallIntegerField(default=0)
    rating                  = models.SmallIntegerField(default=1)
    
    class Meta(object):
        verbose_name = _('Soa')
        verbose_name_plural = _('Soas')

    def __str__(self):
        return self.client_name
        

'''
@python_2_unicode_compatible
class ReviewOrderAgreement(TimeStampedModel):
    """
    Model for Review Order Agreement
    """
    APPROVAL_CHOICES = (
        ('1', 'Approve SOA'),
        ('2', 'Approve SOA when changes made'),
        ('3', 'SOA requires changes'),
    )

    soa_order = models.ForeignKey(Soa, related_name="soa_order")
    #soa_type = models.ForeignKey(SoaType, related_name="soa_type")
    is_approved = models.BooleanField(_('Is Approved?'), default=False)
    is_submit = models.BooleanField(_('Send for approval?'), default=False)
    is_completed = models.BooleanField(_('Is Completed?'), default=False)
    paraplanner_approver =  models.ForeignKey(User, **optional)
    comments = models.TextField(_('Comments'), **optional)
    approval_choice = models.CharField(max_length=1, choices=APPROVAL_CHOICES, **optional)

    class Meta(object):
        verbose_name = _('Review Soa')
        verbose_name_plural = _('Review Soas')

    def __str__(self):
        return self.soa_order.client_name
'''
# Create models for Goal, GoalType, File, FileType