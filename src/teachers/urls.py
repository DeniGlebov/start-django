from django.urls import path

from . import views


app_name = 'teachers'

urlpatterns = [
    path('', views.teacher),
    path('create1/', views.create_teacher),
]
