from rest_framework import generics
from core.models import MenuItem, Category
from core.serializers import MenuItemSerializer, CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
