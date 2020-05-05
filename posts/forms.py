from django import forms 
from .models import post
from website.models import shift, schedule

class requestPost(forms.ModelForm):
    class Meta:
        model = post
        fields = ['shift', 'recipient_shift', 'comment']
        

