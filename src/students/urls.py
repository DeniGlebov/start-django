from django.urls import path

from students import views

app_name = 'students'
urlpatterns = [
    path('list/', views.students, name='list'),
    path('create/', views.create_student, name='create'),
    path('edit/<int:pk>', views.edit_student, name='edit'),
    path('delete/<int:pk>', views.delete_student, name='delete'),
]
