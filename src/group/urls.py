from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('', views.groups_all),
    path('create/', views.create_group),
]
