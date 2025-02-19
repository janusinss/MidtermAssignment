from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('page2/', views.page2),
    # path('addStudent/', views.addStudent, name='addStudent'),
    # path('editStudent/<int:id>/', views.editStudent, name='editStudent'),
    # path('editStudent/<int:id>/updateStudent/', views.updateStudent, name='updateStudent'),
    # path('deleteStudent/<int:id>/', views.deleteStudent, name='deleteStudent')

    path('', views.index),
    path('editPage/', views.editPage),
    path('addStudent/', views.addStudent),
    path('editStudent/<int:id>/', views.editStudent),
    path('editStudent/<int:id>/updateStudent/', views.updateStudent),
    path('deleteStudent/<int:id>/', views.deleteStudent)
]