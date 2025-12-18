from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "price", "stock"]
    list_editable = ['price', 'name']
    ordering = ['id']
    
    
admin.site.register(Product, ProductAdmin)