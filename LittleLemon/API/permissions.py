from rest_framework import permissions

class IsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if not request.user:
            return False
        
         
        return request.user.groups.filter(name='manager').exists()
class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Delivery Crew').exists()