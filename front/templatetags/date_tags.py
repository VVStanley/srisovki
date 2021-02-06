from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def days_passed(created_at):
    '''Получаем сколько дней прошло'''
    return int((timezone.now() - created_at).days)
