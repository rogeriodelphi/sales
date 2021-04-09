from django.urls import path

from core.erp.views import myfirstview, mysecondview

app_name = 'erp'

urlpatterns = [
    path('um/', myfirstview, name='vista1'),
    path('dois/', mysecondview, name='vista2')
]
