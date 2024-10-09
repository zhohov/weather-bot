from django.db import models


class Log(models.Model):
    telegram_user = models.ForeignKey(
        'users.TelegramUser',
        related_name='logs',
        on_delete=models.CASCADE,
    )
    command = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Weather log"
        verbose_name_plural = "Weather logs"

