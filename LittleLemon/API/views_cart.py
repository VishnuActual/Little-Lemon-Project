from rest_framework import generics, status
from rest_framework.response import Response
from .models import CartMenuItem
from .serializers import CartMenuItemSerializer
from .custom_authentications import CustomTokenAuthentication

class CartMenuItemListCreateView(generics.ListCreateAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = CartMenuItemSerializer

    def get_queryset(self):
        return CartMenuItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartMenuItemDeleteView(generics.DestroyAPIView):
    authentication_classes = [CustomTokenAuthentication]

    def delete(self, request, *args, **kwargs):
        cart_items = CartMenuItem.objects.filter(user=request.user)
        print(cart_items) 
        for item in cart_items:
            item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['DELETE'])
# @authentication_classes([CustomTokenAuthentication])
# def delete_cart_menu_items(request):
#     CartMenuItem.objects.filter(user=request.user).delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
