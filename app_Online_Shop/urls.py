from django.urls import path
from .views import HomePageView,ShopListView


urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('HomePage/', ShopListView.as_view(),name='HomePage'),
    # path('', InfoView.as_view(), name='info'),
    # path('info/',)
]
