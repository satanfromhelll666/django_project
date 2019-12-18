from django import forms
from .models import intro

class intro_form(forms.ModelForm):
    class Meta:
        model = intro
        fields =[
            'name',
            'email',
            'address',
            'contatc_num'

        ]