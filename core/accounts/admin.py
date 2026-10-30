from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser')

    searching_filds = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {
            'fields':(
                'email',
                'password'
            )
        }),
    )

admin.site.register(User,CustomUserAdmin)


