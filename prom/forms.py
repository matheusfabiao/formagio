from django import forms

from .models import PromGuest


class ConfirmPresenceForm(forms.Form):
    guest = forms.ModelChoiceField(
        queryset=PromGuest.objects.all().order_by('first_name', 'last_name'),
        label='Selecione seu nome',
    )
    confirm = forms.BooleanField(label='Estou ciente e confirmo minha presença.')
