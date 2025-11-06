from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from .forms import ConfirmPresenceForm
from .models import PromGuest


class PromHomeView(ListView):
    model = PromGuest
    template_name = 'prom/prom_home.html'
    context_object_name = 'confirmed_guests'

    def get_queryset(self):
        return PromGuest.objects.filter(confirmed_presence=True).order_by('-id')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ConfirmPresenceForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ConfirmPresenceForm(request.POST)
        if form.is_valid():
            guest = form.cleaned_data['guest']
            guest.confirmed_presence = True
            guest.save()
        return redirect('prom_thanks')


class PromGuestsView(ListView):
    model = PromGuest
    template_name = 'prom/guests.html'
    context_object_name = 'guests'

    def get_queryset(self):
        return PromGuest.objects.filter(confirmed_presence=True).order_by('first_name', 'last_name')


class PromSuccessView(TemplateView):
    template_name = 'prom/presence_success.html'
