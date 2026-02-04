from django.shortcuts import render
from rest_framework import generics, response, status

from .models import Store, Product, User
from .serializers import StoreSerializer, ProductSerializer, UserSerializer

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = "store_id"

class StoreDeleteAll(generics.DestroyAPIView):
    def delete(self, request, args, **kwargs):
        Store.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "user_id"

class UserDeleteAll(generics.DestroyAPIView):
    def delete(self, request,args, **kwargs):
        User.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)