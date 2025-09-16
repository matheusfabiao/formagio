from django import forms

from .models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['picture', 'name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
