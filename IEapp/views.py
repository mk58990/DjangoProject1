from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Foodsales
from .serializer import FoodsalesSr
# Create your views here.

class FoodFilter(APIView):
    def get(self,r,Product):
        fooddetails=Foodsales.objects.filter(Product__iexact=Product)
        serobj=FoodsalesSr(fooddetails,many=True)
        return Response(serobj.data)

    def post(self,r,Product):
        fooddetails=Foodsales.objects.filter(Product__iexact=Product)[0:5]
        serobj=FoodsalesSr(fooddetails,many=True)
        return Response(serobj.data)