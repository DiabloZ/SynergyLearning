from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from News.models import News, Human, Category, Profession


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = "__all__"


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published', 'category']
    fields = ('title', 'content', 'photo',)
    form = NewsAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class HumanAdmin(admin.ModelAdmin):
    list_display = ('surnameName', 'firstName', 'middleName', 'old', 'birthDay', 'profession')
    list_display_links = ('surnameName', 'firstName', 'middleName')
    search_fields = ('surnameName', 'firstName', 'middleName', 'old', 'birthDay', 'profession')
    list_filter = ('profession', 'id')
    list_editable = ['profession']


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Human, HumanAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profession, ProfessionAdmin)
