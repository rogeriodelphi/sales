from django.shortcuts import render

from core.erp.models import Category, Product


def myfirstview(request):
    template_name = 'index.html'
    data = {
        'name': 'Rogerio Martins',
        'categories': Category.objects.all()
    }
    return render(request, template_name, data)


def mysecondview(request):
    template_name = 'second.html'
    data = {
        'name': 'Rogerio Martins',
        'products': Product.objects.all()
    }
    return render(request, template_name, data)
