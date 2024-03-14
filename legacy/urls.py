from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('users/', include('users.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),   
]
