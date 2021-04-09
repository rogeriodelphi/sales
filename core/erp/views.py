from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def myfirstview(request):
    data = {
        'name': 'Rogerio Martins'
    }
    return render(request, 'index.html', data)