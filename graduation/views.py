from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import GuestForm
from .models import Guest


class HomeView(FormView):
    template_name = 'graduation/home.html'
    form_class = GuestForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guests'] = Guest.objects.all()[:3]
        return context

    def form_valid(self, form):
        if form.errors:
            return super().form_invalid(form)
        form.save()
        return super().form_valid(form)


class GuestListView(ListView):
    model = Guest
    template_name = 'graduation/guest_list.html'
    context_object_name = 'guests'

    def get_queryset(self):
        search = self.request.GET.get('search')

        if search:
            guests = Guest.objects.filter(name__icontains=search)
        else:
            guests = Guest.objects.all()

        return guests
