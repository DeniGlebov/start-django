import random

from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generate random students'  # noqa

    def handle(self, *args, **options):
        fake = Faker()
        students = []
        for _ in range(1000):
            students.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(20, 40),
            ))

        Student.objects.bulk_create(students)
