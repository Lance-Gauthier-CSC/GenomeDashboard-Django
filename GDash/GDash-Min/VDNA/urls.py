from django.urls import path
from . import views

urlpatterns = [
    path('', views.VDNA, name='VDNApage'),
]