from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Akobir_1/', admin.site.urls),
    path('temp/', include('temp.urls')),
    path('users/', include('users.urls')),
    path('', include('homepage.urls')),
    path('page',include('app_Online_Shop.urls')),
]
