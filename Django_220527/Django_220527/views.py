from django.http import HttpResponse
from django.shortcuts import render


def inedx_views(request):
    return render(request, 'index.html')