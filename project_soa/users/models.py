# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

optional = {
    "null": True,
    "blank": True,
}


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    is_paraplanner = models.BooleanField(_('Is Paraplanner?'), default=False)
    account_name = models.CharField(_('Account Name'), max_length=254, **optional)
    bsb = models.CharField(_('BSB'), max_length=254, **optional)
    account_number = models.CharField(_('Account Number'), max_length=254, **optional)
    
    '''
    # Fields only for Adviser
    isCfp = models.BooleanField(_('Is Certified Financial Planner?'), default=True)
    businessLine1 = models.CharField(_("Business Line 1"), blank=True, max_length=255)
    businessLine2 = models.CharField(_("Business Line 2"), blank=True, max_length=255)
    businessLine3 = models.CharField(_("Business Line 3"), blank=True, max_length=255)
    businessLine4 = models.CharField(_("Business Line 4"), blank=True, max_length=255)
    
    emailAddress = models.EmailField(_('Email Address'), max_length=50, **optional)
    mobilePhone = models.CharField(_('Mobile Phone'), max_length=50, **optional)
    homePhone = models.CharField(_('Home Phone'), max_length=50, **optional)
    addressLine1 = models.CharField(_('Address Line 1'), max_length=255, **optional)
    addressLine2 = models.CharField(_('Address Line 2'), max_length=255, **optional)
    addressLine3 = models.CharField(_('Address Line 3'), max_length=255, **optional)
    authRepLine1 = models.CharField(_('Authorized Representative Line 1'), max_length=255, **optional)
    authRepLine2 = models.CharField(_('Authorized Representative Line 2'), max_length=255, **optional)
    authRepLine3 = models.CharField(_('Authorized Representative Line 3'), max_length=255, **optional)
    authRepLine4 = models.CharField(_('Authorized Representative Line 4'), max_length=255, **optional)
    '''
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
