from django.db import models


class TelegramUser(models.Model):
    telegram_user_id = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"

