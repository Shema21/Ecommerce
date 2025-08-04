from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'status', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['status', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    