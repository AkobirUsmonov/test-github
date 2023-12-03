from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Online_Shop
# from django.forms import model_to_dict
# from rest_framework.views import APIView
# from rest_framework.response import Response
# Create your views here.

class ShopListView(ListView):
    model = Online_Shop
    template_name = 'HomePage.html'


class HomePageView(TemplateView):
    def get(self, request):
        context = {}
        clay = Online_Shop.objects.all()
        context['data'] = clay
        return render(request, 'home.html', context)

# class InfoView(TemplateView):
#     def get(self, request):
#         context = {}
#         clay = Online_Shop.objects.all()
#         context['data'] = clay
#         return render(request, 'info.html', context)




# class CarsView(APIView):
#     def get(self, request):
#         try:
#             pass_score = request.GET['pass_score']
#             cars = Cars.objects.filter(
#                 votes__gte=pass_score).values()
#         except:
#             cars = Cars.object.all().values()
#         return Response({'cars': list(cars)})

#     def post(self, request):
#         new_car = Cars.object.create(
#             first_name=request.data['first_name'],
#             last_name=request.data['last_name'],
#             votes=request.data['exam_mark'],
#         )
#         return Response({'new_car': model_to_dict(new_car)})

#     def delete(self, request):
#         try:
#             car_id = request.GET['car_id']
#             Cars.objects.filter(pk=car_id).delete()
#             return Response({'result': 'success', 'desc': f'Car with id:    {car_id} successfully deleted'})
#         except:
#             return Response({'result': 'error', 'desc': 'Internal Server Error! Please try again later...'})
