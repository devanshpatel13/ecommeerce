from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Customer)
class CustomerregistrationAdmin(admin.ModelAdmin):
    list_display = ["username","email","contact","users"]


@admin.register(Shopowner)
class ShopownerAdmin(admin.ModelAdmin):
    list_display = ["name","og_price","image","descripation","discount","sellprice","discountprice"]


@admin.register(Cart)
class CartAmdin(admin.ModelAdmin):
    list_display = ["user","cart_id"]

@admin.register(Myorder)
class MyorderAmdin(admin.ModelAdmin):
    list_display = ["user","product","quantity","date","status"]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["user","first_name","last_name","address","city","state","pincode"]

@admin.register(cart_item)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user","cart","product","quantity"]

#
# @admin.register(Cart_itme)
# class Cart_itemAdmin(admin.ModelAdmin):
#     list_display = ["user","product","cart","quantity"]


# admin.site.register(Coupon)
admin.site.register(Couponcode)
