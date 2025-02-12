from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = ('product_name', 'product_price','category','is_available')
    list_filter = ('product_name','product_price')
    search_fields = ('product_name','category')
admin.site.register(Product, ProductAdmin)