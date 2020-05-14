from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('list/', views.groups_all, name='list'),
    path('create/', views.create_group, name='create'),
    path('edit/<int:pk>', views.edit_group, name='edit'),
]
