from django.urls import path

from . import views

app_name = 'group'
urlpatterns = [
    path('', views.groups_all),
]
