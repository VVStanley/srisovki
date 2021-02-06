from django import template

register = template.Library()


@register.filter
def toconsole(value):
    print(value)
    print(dir(value))
    return '123123'
