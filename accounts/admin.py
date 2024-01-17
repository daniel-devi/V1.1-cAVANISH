from django.contrib import admin
from .models import Tenant
from django.contrib import messages
from django.contrib.admin import ModelAdmin

# Register your models here.
class TenanatModelAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, "A New Tenant has Created an Account, Give him a Room")
        
admin.site.register(Tenant)