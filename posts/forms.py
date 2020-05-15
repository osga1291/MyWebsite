from django import forms 
from .models import post
from website.models import shift, schedule
from users.models import User, Profile
from django.db.models import Q
from django.shortcuts import get_object_or_404
class requestPost(forms.Form):
    recipient = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = User.objects.all()
    )
    comment = forms.CharField(max_length=100)
    def __init__(self,*args, **kwargs):
        shift_input = kwargs.pop('shift_instance', None)
        options = shift_input.check_cover
        super(requestPost,self).__init__(*args,**kwargs)
        #print(User.objects.filter(profile__roles__name = "Manager"))
        
        print(options)
        self.fields['recipient'].choices = options
        


