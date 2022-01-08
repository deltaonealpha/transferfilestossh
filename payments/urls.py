# payments/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('/payment', views.home_view, name='payments-home'),
]