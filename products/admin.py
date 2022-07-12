from django.contrib import admin

from .models import Category, Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'image', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Comment)
