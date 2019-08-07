from django.contrib import admin
from .models import Category, Product, Service, Support, Feedback

admin.site.site_header = 'Dell Recommend Administration'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'comments']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
