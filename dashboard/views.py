from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from content.models import Movie, TvShow
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data_movie(request):
    dataset = Movie.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def pivot_data_tvshow(request):
    dataset = TvShow.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)