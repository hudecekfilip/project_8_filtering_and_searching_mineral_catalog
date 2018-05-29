from django import template

from django.http import HttpResponseRedirect

from minerals.models import Mineral

register = template.Library()

@register.inclusion_tag('minerals/minerals_names.html')
def first_letters():
    all = Mineral.objects.all()
    list = []
    list2 = []
    for x in all:
        list.append(x.name)
    for x in list:
        list2.append(x[0])
    hovno = "hovno"
    newlist = sorted(set(list2), key=lambda x:list2.index(x))
    return {'newlist': newlist}
