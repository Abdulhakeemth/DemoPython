from . models import  Task
from django import forms

class TodOForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']