from celery import shared_task


@shared_task
def slow_func(num=10):
    from time import sleep
    sleep(num)


@shared_task
def periodic(num=10):
    # print('Hello\n' * 3)
    pass


@shared_task
def print_student(student_id):
    # from students.models import Student
    # student = Student.objects.get(id=student_id)
    # print(student.id, student.first_name, student.last_name)
    pass


@shared_task
def delete_logs():  # after 7 day
    import datetime
    from students.models import Logger

    time_temp = datetime.datetime.now().date() - datetime.timedelta(days=6)
    year = time_temp.strftime("%Y")
    month = time_temp.strftime("%m")
    day = time_temp.strftime("%d")

    Logger.objects.filter(created__date__lt=datetime.date(int(year), int(month), int(day))).delete()


@shared_task
def send_mail_contact_us(msg):
    from django.core.mail import send_mail
    send_mail('New feedback', msg, 'enttestov2579532@gmail.com', ['dmytro.kaminskyi92@gmail.com'])
