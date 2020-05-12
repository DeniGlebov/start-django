from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('hello-word/', views.hello_world),
    # path('students-list/', views.students, name='students-list'),
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    # path('student-create/', views.create_student, name='student-create'),

    path('students/', include('students.urls')),

    path('teachers/', include('teachers.urls')),
    path('group/', include('group.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
