from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"
        ordering = ['-created_at']
