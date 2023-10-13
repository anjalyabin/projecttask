from django import forms
from . models import

class regform(forms.ModelForm):
    class Meta:
        model=MyModel
        fields=['name','date','age','mobile','address']