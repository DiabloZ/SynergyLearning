from News.models import Category, Profession
from django import template

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('News/list_categories.html')
def show_categories(arg1='Category', arg2='list'):
    categories = get_categories()
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}
