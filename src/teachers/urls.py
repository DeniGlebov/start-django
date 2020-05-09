from django.urls import path

from . import views

# path('teachers/', include('teachers.urls')),


app_name = 'teachers'
urlpatterns = [
    path('', views.teacher),
]
