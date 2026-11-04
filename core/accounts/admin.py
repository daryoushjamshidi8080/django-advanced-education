from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserCreationForm



class CustomUserAdmin(UserAdmin):
    """
        class add new users in admin pannel 
    """
    model = User
    add_form = CustomUserCreationForm
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser')

    searching_filds = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {
            'fields':('email','password')
        }),('permissions',
            {'fields':('is_staff', 'is_active', 'is_superuser'),}
        ),('group permissions',
            {'fields':('groups', 'user_permissions'),}
        ),('important date',
            {'fields':('last_login', ),}
        )
    )

    add_fieldsets = (
            (None, {
                'classes':('wide'),
                'fields':('email','password1','password2', 'is_staff', 'is_active', 'is_superuser')
            }),
        )
admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)



