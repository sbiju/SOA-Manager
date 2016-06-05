from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
#from django_countries import CountryField
from model_utils.models import TimeStampedModel
# Other models
from project_soa.users.models import User
from soamgr.models import Soa, SoaType, Strategy, Goal

optional = {
    "null": True,
    "blank": True,
}


@python_2_unicode_compatible
class Client(models.Model):
    """
    Models for Adviser Clients
    """
    clientID = models.CharField(_('Client Name'), max_length=254, unique=True)
    xplanID = models.CharField(_('XPLAN ID'), max_length=20)
    #clientAdviser = models.ForeignKey(User, related_name="clientAdviser")
    
    title = models.CharField(_('Title'), max_length=20, **optional)
    lastName = models.CharField(_('Last Name'), max_length=50)
    middleName = models.CharField(_('Middle Name'), max_length=50, **optional)
    firstName = models.CharField(_('First Name'), max_length=50)
    secondName = models.CharField(_('Second Name'), max_length=50, **optional)
    preferredName = models.CharField(_('Preferred Name'), max_length=50, **optional)
    fullName = models.CharField(_('Full Name'), max_length=254)
    completeName = models.CharField(_('Complete Name'), max_length=254)
    
    photo = models.CharField(_('Photo'), max_length=1000, **optional)
    email = models.EmailField(_('Email Address'), max_length=50)
    mobilePhone = models.CharField(_('Mobile Phone'), max_length=50)
    homePhone = models.CharField(_('Home Phone'), max_length=50)
    addressLine1 = models.CharField(_('Address Line 1'), max_length=255, **optional)
    addressLine2 = models.CharField(_('Address Line 2'), max_length=255, **optional)
    addressLine3 = models.CharField(_('Address Line 3'), max_length=255, **optional)
    
    gender = models.CharField(_('Gender'), max_length=1, choices=(('M','Male'),('F','Female'),), **optional)
    birthDate = models.DateField(_('Birth Date'))
    deathDate = models.DateField(_('Death Date'))
    maritalStatus = models.CharField(_('Marital Status'), max_length=1, choices=(('S','Single'),('M','Maried'),('D','Divorced'),('W', 'Widower'),), **optional)
    religion = models.CharField(_('Religion'), max_length=50)
    #nationality = CountryField()
    occupation = models.CharField(_('Title'), max_length=50, **optional)
    income = models.DecimalField(_('Income'), max_digits=20, decimal_places=2)    
    
    health = models.CharField(_('Health Condition'), max_length=254, **optional)
    isSmoker = models.BooleanField(_('Is Smoker?'), default=False)
    willExists = models.BooleanField(_('Will Exists?'), default=False)
    powerOfAttorney = models.CharField(_('Health Condition'), max_length=254, **optional)   
    
    DefaultTemplate = models.CharField(_('Default Template'), max_length=254, **optional) # Lookup to Templates Table
    DefaultFormatting = models.CharField(_('Default Formatting'), max_length=254, **optional) # Lookup to Formatting Table
    DefaultStrategies = models.CharField(_('Default Strategies'), max_length=2000, **optional) # Multiple Select the Strategies Table
    
    class Meta(object):
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        
    #def get_absolute_url(url):
    #    return reverse('clientmgr:client_update', kwargs={'pk', self.pk})

    def __str__(self):
        return self.clientID + ': ' + self.completeName


@python_2_unicode_compatible
class Partner(models.Model):
    """
    Models for Client's Partner
    """
    partnerID = models.CharField(_('Client Name'), max_length=254)
    xplanID = models.CharField(_('XPLAN ID'), max_length=20)
    #partnerAdviser = models.ForeignKey(User, related_name="partnerAdviser")
    #partnerClient = models.ForeignKey(Client, related_name="partnerClient")
    
    title = models.CharField(_('Title'), max_length=20, **optional)
    lastName = models.CharField(_('Last Name'), max_length=50)
    middleName = models.CharField(_('Middle Name'), max_length=50, **optional)
    firstName = models.CharField(_('First Name'), max_length=50)
    secondName = models.CharField(_('Second Name'), max_length=50, **optional)
    preferredName = models.CharField(_('Preferred Name'), max_length=50, **optional)
    fullName = models.CharField(_('Full Name'), max_length=254)
    completeName = models.CharField(_('Complete Name'), max_length=254)
    
    photo = models.CharField(_('Photo'), max_length=1000, **optional)
    email = models.EmailField(_('Email Address'), max_length=50)
    mobilePhone = models.CharField(_('Mobile Phone'), max_length=50)
    homePhone = models.CharField(_('Home Phone'), max_length=50)
    addressLine1 = models.CharField(_('Address Line 1'), max_length=255, **optional)
    addressLine2 = models.CharField(_('Address Line 2'), max_length=255, **optional)
    addressLine3 = models.CharField(_('Address Line 3'), max_length=255, **optional)
    
    gender = models.CharField(_('Gender'), max_length=1, choices=(('M','Male'),('F','Female'),), **optional)
    birthDate = models.DateField(_('Birth Date'))
    deathDate = models.DateField(_('Death Date'))
    maritalStatus = models.CharField(_('Marital Status'), max_length=1, choices=(('S','Single'),('M','Maried'),('D','Divorced'),('W', 'Widower'),), **optional)
    religion = models.CharField(_('Religion'), max_length=50)
    #nationality = CountryField()
    occupation = models.CharField(_('Title'), max_length=50, **optional)
    income = models.DecimalField(_('Income'), max_digits=20, decimal_places=2)    
    
    health = models.CharField(_('Health Condition'), max_length=254, **optional)
    isSmoker = models.BooleanField(_('Is Smoker?'), default=False)
    willExists = models.BooleanField(_('Will Exists?'), default=False)
    powerOfAttorney = models.CharField(_('Health Condition'), max_length=254, **optional)
    
    DefaultTemplate = models.CharField(_('Default Template'), max_length=254, **optional) # Lookup to Templates Table
    DefaultFormatting = models.CharField(_('Default Formatting'), max_length=254, **optional) # Lookup to Formatting Table
    DefaultStrategies = models.CharField(_('Default Strategies'), max_length=2000, **optional) # Multiple Select the Strategies Table

    class Meta(object):
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')

    def __str__(self):
        return self.partnerID + ': ' + self.completeName
        

@python_2_unicode_compatible
class Entity(models.Model):
    """
    Models for Client's Entities
    """
    entityID = models.CharField(_('Client Name'), max_length=254)
    xplanID = models.CharField(_('XPLAN ID'), max_length=20)
    #entityClient = models.ForeignKey(Client, related_name="entityClient")
    
    name = models.CharField(_('Entity Name'), max_length=255)
    description = models.CharField(_('Entity Description'), max_length=255, **optional)
    entType = models.CharField(_('Entity Type'), choices=(('SMSF','Self-Managed Super Fund'),('TF','Trust Fund'),('C','Company'),), max_length=255)
    
    # Could be moved to another model - Financial Details or sth
    incomes = models.DecimalField(_('Income'), max_digits=20, decimal_places=2)  
    expenses = models.DecimalField(_('Expense'), max_digits=20, decimal_places=2)  
    investments = models.DecimalField(_('Investments'), max_digits=20, decimal_places=2)  
    assets = models.DecimalField(_('Assets'), max_digits=20, decimal_places=2)  
    debts = models.DecimalField(_('Debts'), max_digits=20, decimal_places=2)  
    netFinancial = models.DecimalField(_('Net Financial Position'), max_digits=20, decimal_places=2)  
    defensiveAssets = models.FloatField(_('Defensive Assets'))
    growthAssets = models.FloatField(_('Growth Assets'))
    riskProfile = models.CharField(_('Risk Profile'), max_length=100)
    assessment = models.CharField(_('Assessment'), max_length=100)
    about = models.CharField(_('About'), max_length=255)
    
    class Meta(object):
        verbose_name = _('Entity')
        verbose_name_plural = _('Entities')

    def __str__(self):
        return self.entityID + ': ' + self.name + ' (' + self.entType + ')'