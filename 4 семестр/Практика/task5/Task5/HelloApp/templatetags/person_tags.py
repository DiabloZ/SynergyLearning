from django import template

from HelloApp.models import Person

register = template.Library()


@register.simple_tag(name="get_list_people")
def get_people():
    return Person.objects.all()

@register.inclusion_tag('HelloScreen/hello_person.html')
def show_people(arg1='Список приветствия', arg2=''):
    people = get_people()
    return {'people': people, 'arg1': arg1, 'arg2': arg2}