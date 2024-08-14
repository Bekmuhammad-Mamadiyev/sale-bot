from django.contrib import admin

# Register your models here.
from users.models import Profile, Product, Sale

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'client_name', 'create_at', 'qty',)