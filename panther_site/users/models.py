from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class TgUserManager(UserManager):
    def create_user(self, username, password, chat_id, first_name, last_name, tg_username):

        user = self.model(
            username=username,
            chat_id=chat_id,
            first_name=first_name,
            last_name=last_name,
            tg_username=tg_username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def __str__(self):
        return self.username


class TgUser(AbstractUser):
    chat_id = models.BigIntegerField(null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    tg_username = models.CharField(max_length=255, null=True, blank=True)

    objects = TgUserManager()
