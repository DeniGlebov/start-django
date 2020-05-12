from django.urls import path

from . import views


app_name = 'teachers'

urlpatterns = [
    path('', views.teacher),
    path('create/', views.create_teacher),
]
