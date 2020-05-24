import random
from datetime import datetime

from django.core.management.base import BaseCommand

from faker import Faker

from group.models import Group

from students.models import Student

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random students'  # noqa

    def handle(self, *args, **options):
        fake = Faker()
        students = []
        for _ in range(100):
            students.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(20, 40),
            ))

        Student.objects.bulk_create(students)
        course = ['PHP', 'Java', 'Python', 'Ruby', 'Rust', 'Swift', 'Linux', 'Introduction']

        for i in range(10):
            s = Student.objects.order_by('?').last()
            c = Teacher.objects.order_by('?').last()

            Group.objects.create(
                course=random.choice(course),
                number_students_in_group=random.randint(3, 15),
                head_id=s.id,
                curator_id=c.id,
                start_group=(fake.date_between_dates(date_start=datetime(2020, 5, 23), date_end=datetime(2020, 12, 23)))
            )
