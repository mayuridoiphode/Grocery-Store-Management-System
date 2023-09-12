from django.shortcuts import render
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated


# Create your views here.
class DemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response({'success': "Hurray you are authenticated"})


class ProductView(APIView):

    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_exact=category)
        else:
            queryset = Product.objects.all()

        # queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})
