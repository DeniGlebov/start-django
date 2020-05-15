import random

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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

    return render(request, 'teachers-list.html', context={'teachers': teacher_queryset})


def generate_teacher(request):
    fake = Faker()
    teachers = Teacher.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                      age=(random.randrange(27, 55)))

    response = f'New teacher {teachers.full_info} age<br/>'

    return HttpResponse(response)


def index(request):
    return render(request, 'index.html')


def create_teacher(request):
    from teachers.forms import TeacherCreateForm

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm()

    context = {'create_form': form}

    return render(request, 'teachers-create.html', context=context)


def edit_teacher(request, pk):
    try:
        teach = get_object_or_404(Teacher, id=pk)
    except OverflowError:  # http://127.0.0.1:8000/students/edit/9999999999999999999
        raise Http404

    if request.method == 'POST':
        form = TeacherCreateForm(request.POST, instance=teach)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    elif request.method == 'GET':
        form = TeacherCreateForm(instance=teach)

    context = {'edit_form': form, 'instance': teach}

    return render(request, 'teachers-edit.html', context=context)


def delete_teacher(request, pk):
    teach = get_object_or_404(Teacher, id=pk)
    teach.delete()
    return HttpResponseRedirect(reverse('teachers:list'))
