from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Mineral


def all_minerals(request):
    minerals = Mineral.objects.order_by('name')
    random_mineral = Mineral.objects.order_by('?').first()
    return render(request, 'minerals/index.html', {'minerals': minerals,
                                            'random_mineral': random_mineral})


def mineral_detail(request, pk):
    # Primary Key (PK) is by default ID of the mineral
    mineral = get_object_or_404(Mineral, pk=pk)
    random_mineral = Mineral.objects.order_by('?').first()
    return render(request, 'minerals/detail.html', {'mineral': mineral,
                                            'random_mineral': random_mineral})


def search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(
        Q(name__icontains=term) |
        Q(category__icontains=term) |
        Q(formula__icontains=term) |
        Q(color__icontains=term) |
        Q(luster__icontains=term) |
        Q(streak__icontains=term) |
        Q(crystal_system__icontains=term) |
        Q(unit_cell__icontains=term) |
        Q(crystal_symmetry__icontains=term) |
        Q(cleavage__icontains=term) |
        Q(mohs_scale_hardness__icontains=term) |
        Q(diaphaneity__icontains=term) |
        Q(optical_properties__icontains=term) |
        Q(refractive_index__icontains=term) |
        Q(crystal_habit__icontains=term) |
        Q(specific_gravity__icontains=term) |
        Q(group__icontains=term)
    )
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals})


def filter_by_name(request, letter):
    minerals = Mineral.objects.filter(name__startswith=letter)
    url = request.build_absolute_uri()
    filter = url.split("/filter/", 1)[1]
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals, 'filter': filter})


def filter_by_category(request, category):
    minerals = Mineral.objects.filter(category__iexact=category)
    url = request.build_absolute_uri()
    filter = url.split("/filter/category/", 1)[1]
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals, 'filter': filter})


def other_categories(request):
    minerals = Mineral.objects.filter(category__isnull=False).exclude(category__iexact="Silicate")
    url = request.build_absolute_uri()
    filter = url.split("/filter/category/", 1)[1]
    return render(request, 'minerals/minerals_list.html', {'minerals': minerals, 'filter': filter})
