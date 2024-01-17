from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ModelForm
from .models import Tenant


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class PassWordChangr(PasswordChangeForm):
    class Meta:
        pass
    


class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        exclude = ['user', 'room', 'monthly_pay', 'weekly_pay', 'date_joined']