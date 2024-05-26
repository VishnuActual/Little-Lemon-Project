from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Order, OrderItem, CartMenuItem
from .serializers import OrderSerializer, OrderItemSerializer
from .permissions import IsDeliveryCrew,  IsManager 
from .custom_authentications import CustomTokenAuthentication





class CustomerOrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Get cart items, create order items, and clear cart logic
        cart_items = CartMenuItem.objects.filter(user=self.request.user)
        order = serializer.save(user=self.request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart_items.delete()

class CustomerOrderDetailView(generics.RetrieveAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, id=self.kwargs['orderId'])

class ManagerOrderListView(generics.ListAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        return Order.objects.all()

class ManagerOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        return Order.objects.all()

class DeliveryCrewOrderListView(generics.ListAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsDeliveryCrew]

    def get_queryset(self):
        return Order.objects.filter(delivery_crew=self.request.user)

class DeliveryCrewOrderUpdateView(generics.UpdateAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsDeliveryCrew]

    def get_queryset(self):
        return Order.objects.filter(delivery_crew=self.request.user, id=self.kwargs['orderId'])

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object()
        if 'status' in request.data:
            order.status = request.data['status']
            order.save()
            return Response(OrderSerializer(order).data)
        return Response(status=status.HTTP_400_BAD_REQUEST)