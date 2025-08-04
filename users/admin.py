from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_superuser','last_login','is_staff','is_active','date_joined']
    search_fields = ['username','email']