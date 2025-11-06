from django.urls import path

from .views import PromHomeView, PromSuccessView, PromGuestsView

urlpatterns = [
    path('', PromHomeView.as_view(), name='prom_home'),
    path('confirmados/', PromGuestsView.as_view(), name='prom_guests'),
    path('obrigada/', PromSuccessView.as_view(), name='prom_thanks'),
]
