from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post
from step_drawing.models import PostStepDrawingModel

User = get_user_model()


class Comment(MPTTModel):

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return str(self.id)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name='comments_post')

    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')


class CommentStepDrawingModel(MPTTModel):

    class Meta:
        verbose_name = 'Комментарий пошаговое обучение'
        verbose_name_plural = 'Комментарии пошаговое обучение'
        db_table = 'step_comments'
        ordering = ['created_at']

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return str(self.id)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments_step_user')
    post = models.ForeignKey(PostStepDrawingModel, on_delete=models.CASCADE, null=False, related_name='comments_step_post')

    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
