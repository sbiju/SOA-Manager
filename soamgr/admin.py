from django.contrib import admin

from .models import Soa, SoaType, Strategy, Goal

admin.site.register(Soa)
admin.site.register(SoaType)
admin.site.register(Strategy)
admin.site.register(Goal)
