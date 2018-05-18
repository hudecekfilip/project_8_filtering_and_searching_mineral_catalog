from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = 'minerals'
urlpatterns = [
    path('', views.all_minerals, name='index'),
    path('<int:pk>/', views.mineral_detail, name='detail'),
    path('search/', include('haystack.urls')),
]
