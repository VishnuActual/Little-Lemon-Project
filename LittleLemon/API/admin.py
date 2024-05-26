from django.contrib import admin
from .models import MenuItem, Category, CartMenuItem, Order, OrderItem 

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'featured', 'category')
    search_fields = ('title',)
    list_filter = ('featured', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)

@admin.register(CartMenuItem)
class CartMenuItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_item', 'quantity')  
    search_fields = ('user__username', 'menu_item__title')  
    list_filter = ('user', 'menu_item')  


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']
    list_filter = ['status', 'date']
    search_fields = ['user__username', 'delivery_crew__username']
    readonly_fields = ['id']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'menu_item', 'quantity', 'unit_price', 'price']
    search_fields = ['order__id', 'menu_item__name']
    readonly_fields = ['id']