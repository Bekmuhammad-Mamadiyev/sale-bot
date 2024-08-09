from django.contrib import admin

# Register your models here.
from users.models import Profile

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram',)