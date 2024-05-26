from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if not auth_header:
            return None

        try:
            auth_type, token = auth_header.split(' ')
            if auth_type.lower() != 'bearer':
                raise AuthenticationFailed('Invalid authentication header')
        except ValueError:
            raise AuthenticationFailed('Invalid authentication header')

        try:
            token_obj = Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return (token_obj.user, token_obj)
























































# from rest_framework.authentication import BaseAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# class CustomTokenAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         auth_header = request.META.get('HTTP_AUTHORIZATION')
#         bearer, token = auth_header.split(' ')
#         print(token) 
#         token_obj = Token.objects.get(key=token)
#         return (token_obj.user, token_obj)
        
