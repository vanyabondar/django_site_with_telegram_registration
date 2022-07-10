from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group

from .forms import TgUserChangeForm
from .models import TgUser


class TgUserAdmin(UserAdmin):
    model = TgUser
    form = TgUserChangeForm
    list_display = [
        'username',
        'chat_id',
        'first_name',
        'last_name',
        'tg_username',
    ]
    fieldsets = (
        ('Login', {'fields': ('username', 'password')}),
        ('Telegram Info',
            {'fields': ('chat_id', 'first_name', 'last_name', 'tg_username')}),
        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


admin.site.register(TgUser, TgUserAdmin)
admin.site.unregister(Group)
