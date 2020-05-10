from django.contrib import admin
from django.urls import include, path

from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),

    path('hello-word/', views.hello_world),
    path('students/', views.students),
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('create/', views.create_student),

    path('teachers/', include('teachers.urls')),
    path('group/', include('group.urls')),
]
