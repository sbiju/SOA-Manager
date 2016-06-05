from django.contrib import admin

# Register your models here.
from .models import Template, Subtemplate, Formatting, FormattingDetail

admin.site.register(Template)
admin.site.register(Subtemplate)
admin.site.register(Formatting)
admin.site.register(FormattingDetail)