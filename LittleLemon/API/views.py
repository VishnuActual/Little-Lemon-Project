from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .custom_authentications import CustomTokenAuthentication  
from django.contrib.auth.models import User, Group

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def me(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    bearer, token = auth_header.split(' ')
    print(token) 
    token_obj = Token.objects.get(key=token)
    user = token_obj.user 
    return Response({"username": user.username, "email": user.email}, status=200)

class UserDetailView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"username": user.username, "email": user.email}, status=200)

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)  # Allow partial updates

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response({"message": "User deleted successfully"}, status=200)




class UserManagerAssignmentView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"error": "Only admin users can perform this action"}, status=status.HTTP_403_FORBIDDEN)

        username = request.data.get('username')
        
        if not username:
            return Response({"error": "User_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        manager_group, created = Group.objects.get_or_create(name='manager')
        user.groups.clear()  
        user.groups.add(manager_group)  

        return Response({"message": f"User {user.username} assigned to manager role successfully"}, status=status.HTTP_200_OK)