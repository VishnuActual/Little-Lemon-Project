from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, CartMenuItem, Order, OrderItem



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, default='')
    last_name = serializers.CharField(required=False, allow_blank=True, default='')

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category_id']

    def create(self, validated_data):
        category = validated_data.pop('category')
        menu_item = MenuItem.objects.create(category=category, **validated_data)
        return menu_item

    def update(self, instance, validated_data):
        category = validated_data.pop('category', None)
        if category:
            instance.category = category
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.save()
        return instance
    




class CartMenuItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source='menu_item', write_only=True)

    class Meta:
        model = CartMenuItem
        fields = ['id', 'menu_item', 'menu_item_id', 'quantity', 'price', 'unit_price']
        read_only_fields = ['price', 'unit_price']  # Ensure price and unit_price are read-only

    def create(self, validated_data):
        menu_item = validated_data['menu_item']
        quantity = validated_data['quantity']
        price = menu_item.price * quantity
        unit_price = menu_item.price
        user = self.context['request'].user  # Get the user from the request
        return CartMenuItem.objects.create(
            user=user, menu_item=menu_item, quantity=quantity, price=price, unit_price=unit_price)



from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menu_item', 'quantity', 'unit_price', 'price']
        read_only_fields = ['id']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'items']
        read_only_fields = ['id', 'items']

