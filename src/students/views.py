from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student

import random
import string


# Create your views here.


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
    count = Student.objects.count()  # SELECT COUNT(*) FROM students_student;
    students_queryset = Student.objects.all()  # SELECT * FROM students_student;

    response = f'students: {count}<br/>'

    for student in students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)
