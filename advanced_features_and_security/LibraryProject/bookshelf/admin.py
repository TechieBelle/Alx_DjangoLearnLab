from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class ModelAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'date_of_birth', 'profile_photo')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(User, ModelAdmin)