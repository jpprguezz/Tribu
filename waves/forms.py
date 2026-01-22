from django import forms

from .models import Wave


class EditWavesForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ['content']
