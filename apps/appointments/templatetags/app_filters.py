from django import template
import dateutil

register = template.Library()

#????????
@register.filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    format='%b %d, %Y'
    return date.strftime(format)