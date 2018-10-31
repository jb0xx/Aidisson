from django import forms

from .models import Meal



class MealCreateForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = [
            'trainee',
            'dishes',
            # 'datetime',
        ]
    
    def clean_name(self):
        name = self.cleaned_data.get("trainee")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
