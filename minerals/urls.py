from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = 'minerals'
urlpatterns = [
    path('', views.all_minerals, name='index'),
    path('<int:pk>/', views.mineral_detail, name='detail'),
    path('filter/<slug:letter>/', views.filter_by_name, name='first_letter'),
    path('filter/category/Othe/', views.other_categories, name='other'),
    path('filter/category/<slug:category>/', views.filter_by_category,
    name='category_filter'),
    path('search/', views.search, name='search'),
]
