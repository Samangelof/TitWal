from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_birth', 'country', 'city', 'postal_code', 'full_address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_birth', 'country', 'city', 'postal_code', 'full_address'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
