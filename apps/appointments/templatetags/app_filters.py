from django import template
import dateutil

register = template.Library()
from time import strftime
#????????
@register.filter('formater')
def _jinja2_filter_datetime(date, fmt=None):
    """
    filter that returns the string representation of data instead of pythons default
    """
    return str(date)