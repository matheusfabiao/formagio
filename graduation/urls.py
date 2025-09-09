from django.urls import path

from .views import GuestFormView, GuestListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('convidados/', GuestListView.as_view(), name='guest_list'),
    path('convidados/confirmar/', GuestFormView.as_view(), name='guest_form'),
]
