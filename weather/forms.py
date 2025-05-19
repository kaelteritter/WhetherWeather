from django import forms

from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'location-search-input',
                    'placeholder': 'Населенный пункт...',
                }
            )
        }