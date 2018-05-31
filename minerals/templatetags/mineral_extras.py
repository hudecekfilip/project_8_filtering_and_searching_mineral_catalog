from django import template

from django.template.defaultfilters import stringfilter
from django.http import HttpResponseRedirect
from django import template

from minerals.models import Mineral

register = template.Library()


@register.filter
@stringfilter
def lower(value):
    return value.lower()

@register.filter()
@stringfilter
def remove_last_character(value):
    return value[:-1]


@register.inclusion_tag('minerals/minerals_names.html')
def first_letters():
    names = Mineral.objects.filter(name__isnull=False)
    list = []
    for x in names:
        list.append(x.name[0])
    newlist = sorted(set(list), key=lambda x:list.index(x))
    newlist.remove('c')
    newlist.remove('Å')
    return {'newlist': newlist}


@register.inclusion_tag('minerals/minerals_groups.html')
def group_name():
    # groups = Mineral.objects.filter(Q(category__exact="Oxide") | Q(category__exact="Sulfide"))
    GROUPS = ["Silicates", "Oxides", "Sulfates"]
    return {'groups': GROUPS}
