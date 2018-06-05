from django import template

from django.template.defaultfilters import stringfilter
from django.http import HttpResponseRedirect
from django import template

from minerals.models import Mineral

register = template.Library()


GROUPS = [
    "Silicates", "Oxides", "Sulfates", "Sulfides", "Carbonates", "Halides",
    "Sulfosalts", "Phosphates", "Borates", "Arsenates",
    "Native-Elements", "Other"
]

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
    try:
        newlist.remove('c')
    except ValueError:
        pass
    try:
        newlist.remove('Å')
    except ValueError:
        pass
    return {'newlist': newlist}


@register.inclusion_tag('minerals/minerals_groups.html')
def group_name():
    return {'groups': GROUPS}
