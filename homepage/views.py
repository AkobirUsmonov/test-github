from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Home, Info, About_Us, Online_books

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'HomePage.html'

class InfoView(TemplateView):
    template_name = 'info.html'

class About_UsView(TemplateView):
    template_name = 'about_us.html'

class Online_booksView(TemplateView):
    template_name = 'Online_books.html'

class HomeView(TemplateView):
    def get(self, request):
        context = {}
        clay = Home.objects.all()
        context['data'] = clay
        return render(request, 'HomePage.html', context)

class InfoView(TemplateView):
    def get(self, request):
        context = {}
        clay = Info.objects.all()
        context['books'] = clay
        return render(request, 'info.html', context)


class About_UsView(TemplateView):
    def get(self, request):
        context = {}
        clay = About_Us.objects.all()
        context['books'] = clay
        return render(request, 'about_us.html', context)

class Online_booksView(TemplateView):
    def get(self, request):
        context = {}
        clay = Online_books.objects.all()
        context['books'] = clay
        return render(request, 'Online_books.html', context)