from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовки")
    content = models.TextField(blank=True, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    photo = models.ImageField(upload_to="media/%Y/%m/%d", verbose_name="Фото", blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикован")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def get_absolute_url(self):
        return reverse_lazy('View_news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")

    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Human(models.Model):
    firstName = models.TextField(blank=False, verbose_name="Имя")
    surnameName = models.TextField(blank=False, verbose_name="Фамилия")
    middleName = models.TextField(blank=False, verbose_name="Отчество")
    old = models.IntegerField(verbose_name="Возраст")
    birthDay = models.DateTimeField(verbose_name="День рождения")
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name="Профессия")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания", blank=True)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
        ordering = ['-created_at']


class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Профессия")

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
        ordering = ['title']
