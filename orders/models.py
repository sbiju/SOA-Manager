from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.db.models.signals import post_save

from project_soa.users.models import User
from soamgr.models import SoaType, Soa
from clientmgr.models import Client


optional = {
    "null": True,
    "blank": True,
}


RISK_CHOICES = (
        ('NIL', 'NIL'),
        ('LOW', 'LOW'),
        ('MED', 'MED'),
        ('HIGH', 'HIGH'),
    )


@python_2_unicode_compatible
class Order(models.Model):
    client = models.ForeignKey(Client, related_name='client')
    partner_name = models.CharField(_('Partner Name'), max_length=120, **optional)
    s_type = models.ForeignKey(SoaType, related_name='s_type' , **optional)
    due_date = models.DateField(**optional)
    smsf =models.CharField(_('SMSF'), max_length=50, **optional)
    trust_fund = models.CharField(_('Trust Fund'), max_length=50, **optional)
    company = models.CharField(_('Company'), max_length=50, **optional)
    inside_super = models.CharField(_('Inside Super'), choices=RISK_CHOICES, max_length=50, **optional)
    outside_super = models.CharField(_('Outside Super'), choices=RISK_CHOICES,  max_length=50, **optional)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, **optional)

    def __str__(self):
        return self.company

    class Meta:
        ordering = ["-timestamp"]

    def get_absolute_url(self):
        return reverse('orders:oa-order-detail', kwargs={'pk':self.pk})

