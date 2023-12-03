from django.urls import path
from .views import HomePageView, HomeView, InfoView, About_UsView, Online_booksView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('homepages/', HomeView.as_view(), name='homepages'),
    path('Info/', InfoView.as_view(), name='Info'),
    path('About_Us/', About_UsView.as_view(), name='About_Us'),
    path('Online_books/', Online_booksView.as_view(), name='Online_books'),
]