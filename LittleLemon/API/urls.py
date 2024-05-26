from django.urls import path, include 
from rest_framework.authtoken.views import obtain_auth_token
from .views import register, me, UserDetailView, UserManagerAssignmentView
from .views_menu_item import MenuItemListView, MenuItemDetailView, ManagerMenuItemListView, ManagerMenuItemDetailView
from .views_manager import (
    ManagerUserListView,
    ManagerUserDetailView,
    DeliveryCrewUserListView,
    DeliveryCrewUserDetailView,
)
from .views_cart import CartMenuItemListCreateView, CartMenuItemDeleteView
from .views_order import (CustomerOrderListCreateView, CustomerOrderDetailView,
                          ManagerOrderListView, ManagerOrderDetailView,
                          DeliveryCrewOrderListView, DeliveryCrewOrderUpdateView) 


urlpatterns = [

    path("users/",register, name="register"), 
    path("api-token-auth/",obtain_auth_token), 
    path("users/me/", me, name="user_me"), 
    path("users/details/", UserDetailView.as_view(), name='user_detail'), 
    path("assign-manager/", UserManagerAssignmentView.as_view(), name="user_manager_assignment"),




#----------------------for the menu-items---------------------------------------------------------# 
    path('menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('manager/menu-items/', ManagerMenuItemListView.as_view(), name='manager-menu-item-list'),
    path('manager/menu-items/<int:pk>/', ManagerMenuItemDetailView.as_view(), name='manager-menu-item-detail'),





#----------------------for the manager and delivery crew------------------------------------------# 
    # path('groups/manager/users/', manager_user_list, name='manager-users-list'),
    path('groups/manager/users/', ManagerUserListView.as_view(), name='manager-users-list'),
    path('groups/manager/users/<int:user_id>/', ManagerUserDetailView.as_view(), name='manager-users-detail'),
    path('groups/delivery-crew/users/', DeliveryCrewUserListView.as_view(), name='delivery-crew-users-list'),
    path('groups/delivery-crew/users/<int:user_id>/', DeliveryCrewUserDetailView.as_view(), name='delivery-crew-users-detail'),




#--------------------for the cart and customer ---------------------------------------------------#
    path('cart/menu-items/', CartMenuItemListCreateView.as_view(), name='cart-menu-items-list-create'),
    path('cart/menu-items/', CartMenuItemDeleteView.as_view(), name='cart-menu-items-delete'),
    


#---------------------order management----------------------------------------------------------------------#
    path('orders/', CustomerOrderListCreateView.as_view(), name='customer-order-list-create'),
    path('orders/<int:orderId>/', CustomerOrderDetailView.as_view(), name='customer-order-detail'),
    
    path('manager/orders/', ManagerOrderListView.as_view(), name='manager-order-list'),
    path('manager/orders/<int:orderId>/', ManagerOrderDetailView.as_view(), name='manager-order-detail'),

    path('delivery/orders/', DeliveryCrewOrderListView.as_view(), name='delivery-crew-order-list'),
    path('delivery/orders/<int:orderId>/', DeliveryCrewOrderUpdateView.as_view(), name='delivery-crew-order-update'),


]