from django.urls import path

from . import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.teacher, name='list'),
    path('create/', views.create_teacher, name='create'),
    path('edit/<int:pk>', views.edit_teacher, name='edit'),
]
