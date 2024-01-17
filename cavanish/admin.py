from django.contrib import admin
from .models import Payments,Complains,Rooms,House

# Register your models here.

models = [
    Payments, Complains, Rooms, House, 
]

admin.site.register(models)
