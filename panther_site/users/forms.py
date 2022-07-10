from django.contrib.auth.forms import UserChangeForm

from .models import TgUser


class TgUserChangeForm(UserChangeForm):
    class Meta:
        model = TgUser
        fields = (
            'username',
            'chat_id',
            'first_name',
            'last_name',
            'tg_username'
        )
