from django import forms

from .models import Session



class SessionCreateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
            'trainee',
            'starttime',
            'endtime',
        ]
    
    def clean_name(self):
        name = self.cleaned_data.get("trainee")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
