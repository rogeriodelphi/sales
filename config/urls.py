from django.contrib import admin
from django.urls import path, include

from core.homepage.views import IndexView
from core.login.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('login/', LoginFormView.as_view()),
    path('login/', include('core.login.urls')),
    path('admin/', admin.site.urls),
    path('erp/', include('core.erp.urls')),
]
