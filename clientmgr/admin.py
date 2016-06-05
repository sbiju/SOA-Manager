from django.contrib import admin

# Register your models here.
from .models import Client, Partner, Entity

admin.site.register(Client)
admin.site.register(Partner)
admin.site.register(Entity)