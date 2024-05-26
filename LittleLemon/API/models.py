from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    slug = models.SlugField() 
    title = models.CharField(max_length=255, db_index=True) 


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True) 
    featured = models.BooleanField() 
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1) 


class CartMenuItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for the quantity
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit of the menu item

    def save(self, *args, **kwargs):
        # Calculate price and unit price before saving
        self.price = self.quantity * self.menu_item.price
        self.unit_price = self.menu_item.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.title}"



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew',null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2) 
    date = models.DateField(db_index=True) 

class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField() 
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
    price = models.DecimalField(max_digits=6, decimal_places=2) 

    class Meta:
        unique_together = ('order', 'menu_item') 