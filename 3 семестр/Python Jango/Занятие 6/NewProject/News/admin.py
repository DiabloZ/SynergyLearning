from django.contrib import admin

from News.models import News, Human


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class HumanAdmin(admin.ModelAdmin):
    list_display = ('surnameName', 'firstName', 'middleName', 'old', 'birthDay', 'professions')
    list_display_links = ('surnameName', 'firstName', 'middleName')
    search_fields = ('surnameName', 'firstName', 'middleName', 'old', 'birthDay', 'professions')


admin.site.register(News, NewsAdmin)
admin.site.register(Human, HumanAdmin)
