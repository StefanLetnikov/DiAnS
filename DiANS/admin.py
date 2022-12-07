from django.contrib import admin
from .models import *

# Register your models here.
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("manufacturer_Name",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Manufacturer, ManufacturerAdmin)

class ProductAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

#admin.site.register(Product, ProductAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_filter = ("shop_City",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Shop, ShopAdmin)

class ManufacturerProductAdmin(admin.StackedInline):
    model = ManufacturerProduct
    extra = 0

class ManufacturerProductInline(admin.ModelAdmin):
    inlines = [ManufacturerProductAdmin,]

#admin.site.register(Product, ManufacturerProductInline)

class ShopProductAdmin(admin.StackedInline):
    model = ShopProduct
    extra = 0

class ShopProductInLine(admin.ModelAdmin):
    inlines = [ShopProductAdmin,ManufacturerProductAdmin]

admin.site.register(Product, ShopProductInLine)