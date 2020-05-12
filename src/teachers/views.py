import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from faker import Faker

from teachers.forms import TeacherCreateForm
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


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'create_form': form}

    return render(request, 'teachers_create.html', context=context)
