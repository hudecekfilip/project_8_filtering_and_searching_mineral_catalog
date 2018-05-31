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
        list.append(x.name[0])
    # for x in list:
    #     list2.append(x[0])
    newlist = sorted(set(list), key=lambda x:list.index(x))
    return {'newlist': newlist}
