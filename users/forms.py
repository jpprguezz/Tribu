from django import forms

from .models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'avatar',
            'bio',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
