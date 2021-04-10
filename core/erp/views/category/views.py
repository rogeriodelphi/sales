from django.shortcuts import render

from core.erp.models import Category


def category_list(request):
    data = {
        'title': 'Listagem de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)
