import random

from django.http import HttpResponse
from django.shortcuts import render  # noqa

from faker import Faker

from teachers.models import Teacher


def teacher(request):
    # parse parameters
    param = [
        'age',
        'first_name',
        'last_name',
        'course',
        'id',
    ]

    teacher_queryset = Teacher.objects.all()

    for param in param:
        value = request.GET.get(param)
        if value:
            teacher_queryset = teacher_queryset.filter(**{param: value})

    response = f'teachers: {teacher_queryset.count()}<br/>'

    for teachers in teacher_queryset:
        response += teachers.full_info() + '<br/>'

    return HttpResponse(response)


def generate_teacher(request):
    fake = Faker()
    teachers = Teacher.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                      age=(random.randrange(27, 55)))

    response = f'New teacher {teachers.full_info} age<br/>'

    return HttpResponse(response)
