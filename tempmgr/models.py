from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
#from django_countries import CountryField

from model_utils.models import TimeStampedModel

# Other models
from project_soa.users.models import User
from soamgr.models import Soa, SoaType, Strategy, Goal
from clientmgr.models import Client, Partner, Entity

optional = {
    "null": True,
    "blank": True,
}

# Create your models here.
@python_2_unicode_compatible
class Template(models.Model):
    """
    Model for Soa Templates
    """
    tempID = models.CharField(_('Template ID'), max_length=20)
    tempName = models.CharField(_('Template Name'), max_length=50)
    
    description = models.CharField(_('Description'), max_length=255, **optional)
    tempType = models.CharField(_('Template Type'), max_length=50)
    notes = models.CharField(_('Notes'), max_length=254, **optional)
    udoxTempCombiner = models.CharField(_('Ultradox Template Combiner'), max_length=254)
    udoxFormatSetter = models.CharField(_('Ultradox Formatting Setter'), max_length=254)
    udoxCleanUp = models.CharField(_('Ultradox CleanUp Routine'), max_length=254, **optional)
    udoxDraftUpdater = models.CharField(_('Ultradox Draft Updater'), max_length=254)
    udoxMain = models.CharField(_('Ultradox Main'), max_length=254)
    wksClientData = models.CharField(_('Client Data Worksheet'), max_length=254)
    wksTempData = models.CharField(_('Template Data Worksheet'), max_length=254)
    wksStratData = models.CharField(_('Strategy Data Worksheet'), max_length=254)
        
    class Meta(object):
        verbose_name = _('Soa Template')
        verbose_name_plural = _(' Soa Templates')
    
    #def get_absolute_url(self):
    #    return reverse('tempmgr:detail', kwargs={'pk', self.pk})
        
    def __str__(self):
        return self.tempID + ': ' + self.tempName


@python_2_unicode_compatible
class Subtemplate(models.Model):
    """
    Models for Subtemplates
    """
    subTempID = models.CharField(_('Subtemplate ID'), max_length=20)
    parentTempID = models.CharField(_('Parent Template ID'), max_length=20)
    #parent = models.ForeignKey(Template, on_delete=models.CASCADE)
    
    subTempName = models.CharField(_('Subtemplate Name'), max_length=50)
    description = models.CharField(_('Description'), max_length=255, **optional)
    tempType = models.CharField(_('Template Type'), max_length=50)
    
    isIncluded = models.BooleanField(_('Is Included?'), default=False)
    HasPageBreak = models.BooleanField(_('Has Page Break?'), default=False)
    
    subTempGdocID = models.CharField(_('Subtemplate Google Doc ID'), max_length=254)
    subTempGdocLink = models.CharField(_('Subtemplate Google Doc Link'), max_length=254)
    parentGdocID = models.CharField(_('Parent Template Google Doc ID'), max_length=254)
    parentGdocLink = models.CharField(_('Parent Template Google Doc Link'), max_length=254)
    
    class Meta(object):
        verbose_name = _('Subtemplate')
        verbose_name_plural = _('Subtemplates')

    def __str__(self):
        return self.subTempID + ': ' + self.subTempName
        

@python_2_unicode_compatible
class Formatting(models.Model):
    """
    Models for Formatting
    """
    styleID = models.CharField(_('StyleSet ID'), max_length=20)
    styleName = models.CharField(_('StyleSet Name'), max_length=50)    
    description = models.CharField(_('Description'), max_length=255, **optional)
        
    class Meta(object):
        verbose_name = _('StyleSet')
        verbose_name_plural = _('StyleSets')

    def __str__(self):
        return self.styleID + ': ' + self.styleName


@python_2_unicode_compatible
class FormattingDetail(models.Model):
    """
    Models for Formatting Details
    """
    styleID = models.CharField(_('StyleSet ID'), max_length=20)
    
    title_font = models.CharField(_('Title Font'), max_length=50)
    title_fontsize = models.SmallIntegerField(_('Title FontSize'), default=12)
    title_forecolor = models.CharField(_('Title ForeColor'), max_length=50)
    title_bold = models.BooleanField(_('Title Bold'), default=False)
    title_italic = models.BooleanField(_('Title Italic'), default=False)
    title_alignment = models.CharField(_('Title Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')
    
    subtitle_font = models.CharField(_('Subtitle Font'), max_length=50)
    subtitle_fontsize = models.SmallIntegerField(_('Subtitle FontSize'), default=12)
    subtitle_forecolor = models.CharField(_('Subtitle ForeColor'), max_length=50)
    subtitle_bold = models.BooleanField(_('Subtitle Bold'), default=False)
    subtitle_italic = models.BooleanField(_('Subtitle Italic'), default=False)
    subtitle_alignment = models.CharField(_('Subtitle Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')
    
    h1_font = models.CharField(_('Heading1 Font'), max_length=50)
    h1_fontsize = models.SmallIntegerField(_('Heading1 FontSize'), default=12)
    h1_forecolor = models.CharField(_('Heading1 ForeColor'), max_length=50)
    h1_bold = models.BooleanField(_('Heading1 Bold'), default=False)
    h1_italic = models.BooleanField(_('Heading1 Italic'), default=False)
    h1_alignment = models.CharField(_('Heading1 Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')

    h2_font = models.CharField(_('Heading2 Font'), max_length=50)
    h2_fontsize = models.SmallIntegerField(_('Heading2 FontSize'), default=12)
    h2_forecolor = models.CharField(_('Heading2 ForeColor'), max_length=50)
    h2_bold = models.BooleanField(_('Heading2 Bold'), default=False)
    h2_italic = models.BooleanField(_('Heading2 Italic'), default=False)
    h2_alignment = models.CharField(_('Heading2 Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')

    h3_font = models.CharField(_('Heading3 Font'), max_length=50)
    h3_fontsize = models.SmallIntegerField(_('Heading3 FontSize'), default=12)
    h3_forecolor = models.CharField(_('Heading3 ForeColor'), max_length=50)
    h3_bold = models.BooleanField(_('Heading3 Bold'), default=False)
    h3_italic = models.BooleanField(_('Heading3 Italic'), default=False)
    h3_alignment = models.CharField(_('Heading3 Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')

    h4_font = models.CharField(_('Heading3 Font'), max_length=50)
    h4_fontsize = models.SmallIntegerField(_('Heading3 FontSize'), default=12)
    h4_forecolor = models.CharField(_('Heading3 ForeColor'), max_length=50)
    h4_bold = models.BooleanField(_('Heading3 Bold'), default=False)
    h4_italic = models.BooleanField(_('Heading3 Italic'), default=False)
    h4_alignment = models.CharField(_('Heading3 Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')
    
    h5_font = models.CharField(_('Heading5 Font'), max_length=50)
    h5_fontsize = models.SmallIntegerField(_('Heading5 FontSize'), default=12)
    h5_forecolor = models.CharField(_('Heading5 ForeColor'), max_length=50)
    h5_bold = models.BooleanField(_('Heading5 Bold'), default=False)
    h5_italic = models.BooleanField(_('Heading5 Italic'), default=False)
    h5_alignment = models.CharField(_('Heading5 Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')

    h6_font = models.CharField(_('Heading6 Font'), max_length=50)
    h6_fontsize = models.SmallIntegerField(_('Heading6 FontSize'), default=12)
    h6_forecolor = models.CharField(_('Heading6 ForeColor'), max_length=50)
    h6_bold = models.BooleanField(_('Heading6 Bold'), default=False)
    h6_italic = models.BooleanField(_('Heading6 Italic'), default=False)
    h6_alignment = models.CharField(_('Heading6 Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')

    normal_font = models.CharField(_('Normal Font'), max_length=50)
    normal_fontsize = models.SmallIntegerField(_('Normal FontSize'), default=12)
    normal_forecolor = models.CharField(_('Normal ForeColor'), max_length=50)
    normal_bold = models.BooleanField(_('Normal Bold'), default=False)
    normal_italic = models.BooleanField(_('Normal Italic'), default=False)
    normal_alignment = models.CharField(_('Normal Alignment'), max_length=1, choices=(('L','Left'),('C','Center'),('R','Right'),('J','Justified'),), default='L')

    
    class Meta(object):
        verbose_name = _('StyleSet Detail')
        verbose_name_plural = _('StyleSet Details')

    def __str__(self):
        return self.partnerID + ': ' + self.completeName