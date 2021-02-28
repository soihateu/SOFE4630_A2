from django import forms
from myapp.models import Post

class DateInput(forms.DateInput):
    input_type = 'date'

class Upload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['desc', 'date', 'image']
        widgets = {
            'date': DateInput(),
        }
        