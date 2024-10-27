from django import forms
from hookah.models import HookahTobacco

class TobaccoForm(forms.ModelForm):
    class Meta:
        model = HookahTobacco
        fields = ['image','name','brand','type','description']