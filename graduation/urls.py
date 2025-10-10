from django.urls import path

from .views import GuestListView, HomeView, ThankYouView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('convidados/', GuestListView.as_view(), name='guest_list'),
    path('obrigada/', ThankYouView.as_view(), name='thank_you'),
]
