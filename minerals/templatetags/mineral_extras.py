from django import template

from django.http import HttpResponseRedirect

register = template.Library()

@register.filter
def testicek():
    return HttpResponseRedirect('/minerals/search/search.html')
