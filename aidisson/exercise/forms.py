from django import forms

from .models import Workout


class WorkoutCreateForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = [
            'starttime',
            'endtime',
            'intensity',
        ]
    
    def clean_name(self):
        name = self.cleaned_data.get("trainee")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
    