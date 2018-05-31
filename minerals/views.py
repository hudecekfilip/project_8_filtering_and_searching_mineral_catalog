from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Mineral


def all_minerals(request):
    all_entries = Mineral.objects.order_by('name')
    random_mineral = Mineral.objects.order_by('?').first()
    return render(request, 'minerals/index.html', {'all_entries': all_entries,
                                            'random_mineral': random_mineral})


def mineral_detail(request, pk):
    # Primary Key (PK) is by default ID of the mineral
    mineral = get_object_or_404(Mineral, pk=pk)
    random_mineral = Mineral.objects.order_by('?').first()
    return render(request, 'minerals/detail.html', {'mineral': mineral,
                                            'random_mineral': random_mineral})


def search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals})


def filter_by_name(request, letter):
    minerals = Mineral.objects.filter(name__startswith=letter)
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals})


def filter_by_category(request, category):
    minerals = Mineral.objects.filter(category__iexact=category)
    print(minerals)
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals})
