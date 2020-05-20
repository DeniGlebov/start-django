from celery import shared_task


@shared_task
def slow_func(num=10):
    from time import sleep
    sleep(num)


@shared_task
def periodic(num=10):
    print('Hello\n' * 3)


@shared_task
def print_student(student_id):
    from students.models import Student
    student = Student.objects.get(id=student_id)
    print(student.id, student.first_name, student.last_name)
