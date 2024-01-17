from django.forms import ModelForm
from .models import Complains



class ComplainsForm(ModelForm):
    class Meta:
        model = Complains
        field = "__all__"