from django.db import models
from django.conf import settings


class FeedbackModel(models.Model):

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

    def __str__(self):
        return self.email

    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(verbose_name='Еmail', max_length=150)
    text = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)
