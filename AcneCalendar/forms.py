from django import forms
from django.forms import ModelForm
from .models import AcneModel

class DateInput(forms.DateInput):
    input_type = 'date'

class AcneForm(ModelForm):
    class Meta:
        model = AcneModel
        fields = ['date', 'image', 'desc']
        widgets = {
            'date': DateInput,
            }
