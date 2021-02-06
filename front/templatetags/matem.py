from django import template

register = template.Library()


@register.filter
def plus1(value):
    '''Прибавляем еденицу'''
    return int(value) + 1
