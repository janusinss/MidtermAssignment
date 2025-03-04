from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('editPage/', views.editPage),
    path('addStudent/', views.addStudent),
    path('editStudent/<int:id>/', views.editStudent),
    path('editStudent/<int:id>/updateStudent/', views.updateStudent),
    path('deleteStudent/<int:id>/', views.deleteStudent)
]