from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Note(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.text
