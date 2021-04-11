from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'size', 'material',
                    'category', 'is_available', 'main_photo')
    list_display_links = ('id', 'title')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'category', 'material', 'is_available',)
    search_fields = ('title',)
    ordering = ('is_available',)

    list_per_page = 25


admin.site.register(Product, ProductAdmin)
