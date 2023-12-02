from django import template
from django.db.models import Count

from News.models import Profession

register = template.Library()


@register.simple_tag(name='get_list_professions')
def get_professions():
    return Profession.objects.all()


@register.inclusion_tag('People/list_professions.html')
def show_professions(arg1='Profession', arg2='list'):
    professions = Profession.objects.annotate(cnt=Count('human')).filter(cnt__gt=0)
    return {'professions': professions, 'arg1': arg1, 'arg2': arg2}
