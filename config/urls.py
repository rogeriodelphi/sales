from django.contrib import admin
from django.urls import path, include
from core.homepage.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('core.erp.urls')),
    path('', IndexView.as_view()),
]
