from rest_framework import generics, status
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from .permissions import IsManager
from .custom_authentications import CustomTokenAuthentication

class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes = [CustomTokenAuthentication]

class MenuItemDetailView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes = [CustomTokenAuthentication]

class ManagerMenuItemListView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]
    authentication_classes = [CustomTokenAuthentication]

class ManagerMenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]
    authentication_classes = [CustomTokenAuthentication]
