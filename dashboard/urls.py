from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('datamovie', views.pivot_data_movie, name='pivot_data_movie'),
    path('datatvshow', views.pivot_data_tvshow, name='pivot_data_tvshow'),
]