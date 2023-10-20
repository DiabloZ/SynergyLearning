from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="media/%Y/%m/%d")
    is_published = models.BooleanField(default=True)


class Human(models.Model):
    firstName = models.TextField(blank=False)
    surnameName = models.TextField(blank=False)
    middleName = models.TextField(blank=False)
    old = models.IntegerField()
    birthDay = models.DateTimeField()
    professions = models.TextField(blank=True)