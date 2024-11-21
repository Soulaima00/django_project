from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),  # Homepage (main.html)
    path('reclamation/list', views.reclamation_list, name='reclamation_list'),
    path('reclamation/<int:pk>/detail/', views.reclamation_detail, name='reclamation_detail'),
    path('reclamation/new/', views.reclamation_new, name='reclamation_new'),
    path('reclamation/<int:pk>/edit/', views.reclamation_edit, name='reclamation_edit'),
    path('reclamation/<int:pk>/delete/', views.reclamation_delete, name='reclamation_delete'),
]
