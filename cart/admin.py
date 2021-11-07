from django.contrib import admin
from django.db.models.fields import IntegerField
from .models import CartItem, Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    list_editable = ('is_active',) 

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
