from django import forms

from .models import Log



class WeightCreateForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = [
            'weight',
            'units',
        ]
    
    def clean_name(self):
        name = self.cleaned_data.get("trainee")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
