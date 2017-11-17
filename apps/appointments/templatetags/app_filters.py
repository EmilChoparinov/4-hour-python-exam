from django import template
import dateutil

register = template.Library()
from time import strftime
#????????
@register.filter('formater')
def _jinja2_filter_datetime(date, fmt=None):
    return str(date) + ""