from django import template
import base64
register = template.Library()

@register.filter(name='display_img')
def display_img(_bin):
    if _bin is not None: return _bin.decode('utf-8')


