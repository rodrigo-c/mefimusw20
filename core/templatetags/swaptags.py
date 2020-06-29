from django import template
from random import choice

from core.quotes import quotes

register = template.Library()


@register.filter
def class_name(value):
    return value.__class__.__name__


@register.simple_tag
def random_quote():
    return choice(quotes)

