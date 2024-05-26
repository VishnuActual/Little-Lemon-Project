from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer
from .custom_authentications import CustomTokenAuthentication
from .permissions import IsManager

class ManagerUserListView(generics.ListCreateAPIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsManager]
    queryset = User.objects.filter(groups__name='manager')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.data['user_id'])
        group = Group.objects.get(name='manager')
        user.groups.add(group)
        return Response(status=status.HTTP_201_CREATED)

class ManagerUserDetailView(generics.DestroyAPIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsManager]
    queryset = User.objects.filter(groups__name='manager')

    def delete(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(pk=user_id)
            group = Group.objects.get(name='manager')
            user.groups.remove(group)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeliveryCrewUserListView(generics.ListCreateAPIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsManager]
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.data['user_id'])
        group = Group.objects.get(name='Delivery Crew')
        user.groups.add(group)
        return Response(status=status.HTTP_201_CREATED)

class DeliveryCrewUserDetailView(generics.DestroyAPIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsManager]
    queryset = User.objects.filter(groups__name='Delivery Crew')

    def delete(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(pk=user_id)
            group = Group.objects.get(name='Delivery Crew')
            user.groups.remove(group)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
