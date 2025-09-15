from django.urls import path

from .views import GuestListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('convidados/', GuestListView.as_view(), name='guest_list'),
]
