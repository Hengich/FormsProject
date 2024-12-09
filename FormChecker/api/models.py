from django.db import models

from .consts import MAX_NAME_LENGTH

class FormTemplate(models.Model):
    name = models.CharField(
        verbose_name='Название формы',
        max_length=MAX_NAME_LENGTH,
        unique=True
    )
    fields = models.JSONField()

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
        ordering = 'name',

    def __str__(self):
        return self.name
