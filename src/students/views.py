import random
import string

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from faker import Faker

from students.forms import StudentCreateForm
from students.models import Student


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(choices)

    return password


def hello_world(request):  # from flask import request
    return HttpResponse(
        generate_password(
            int(request.GET['length'])
        )
    )


def students(request):
    # parse parameters
    param = [
        'age',
        'age__gt',
        'first_name',
        'first_name__startswith',
        'last_name',
        'id',
    ]

    students_queryset = Student.objects.all()  # SELECT * FROM students_student;

    for param in param:
        value = request.GET.get(param)
        if value:
            students_queryset = students_queryset.filter(**{param: value})

    # response = f'students: {students_queryset.count()}<br/>'
    #
    # for student in students_queryset:
    #     response += student.info() + '<br/>'
    # return HttpResponse(response)

    return render(request, 'students-list.html', context={'students': students_queryset})


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                     age=(random.randrange(17, 45, 1)))

    response = f'New student ID {student.info()} age<br/>'

    return HttpResponse(response)


def student_generate(count: int = 1) -> str:
    fake = Faker()
    all_response = ''

    for i in range(int(count)):
        student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                         age=(random.randrange(17, 45, 1)))
        response = f'New student ID {student.info()} age<br/>'
        all_response += response

    return HttpResponse(all_response)


def generate_students(request):
    st_count = request.GET['count']
    if st_count.isdigit() and 1 <= int(st_count) <= 100:
        return HttpResponse(student_generate(int(request.GET['count'])))
    else:
        return HttpResponse(f'count value within 1-100')


def index(request):
    # student = Student.objects.order_by('?').last()
    return render(request, 'index.html')


@csrf_exempt
def create_student(request):
    from students.forms import StudentCreateForm

    if request.method == 'POST':
        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    elif request.method == 'GET':
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)


@csrf_exempt
def edit_student(request, pk):
    try:
        student = get_object_or_404(Student, id=pk)
    except OverflowError:  # http://127.0.0.1:8000/students/edit/9999999999999999999
        raise Http404
    # breakpoint()

    # student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    elif request.method == 'GET':
        form = StudentCreateForm(instance=student)

    context = {'form': form}
    # breakpoint()

    return render(request, 'edit.html', context=context)



def delete_student(request, pk):

    student = get_object_or_404(Student, id=pk)
    print(student.id)

    return HttpResponseRedirect(reverse('students:list'))
