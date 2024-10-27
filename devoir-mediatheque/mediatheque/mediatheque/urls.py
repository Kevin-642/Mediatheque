from django.contrib import admin
from django.urls import path, include
from bibliothecaires.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bibliothecaires/', include('bibliothecaires.urls')),
    path('membres/', include('membres.urls')),
    path('', index, name='index'),
]
