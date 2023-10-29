from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовки")
    content = models.TextField(blank=True, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    photo = models.ImageField(upload_to="media/%Y/%m/%d", verbose_name="Фото", blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикован")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Human(models.Model):
    firstName = models.TextField(blank=False, verbose_name="Имя")
    surnameName = models.TextField(blank=False, verbose_name="Фамилия")
    middleName = models.TextField(blank=False, verbose_name="Отчество")
    old = models.IntegerField(verbose_name="Возраст")
    birthDay = models.DateTimeField(verbose_name="День рождения")
    professions = models.TextField(blank=True, verbose_name="Профессия")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания", blank=True)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
        ordering = ['-created_at']