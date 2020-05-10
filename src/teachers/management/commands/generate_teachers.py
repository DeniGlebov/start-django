import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random teacher'  # noqa

    def handle(self, *args, **options):
        fake = Faker()
        course = ['Java', 'C', 'C++', 'Python', 'Linux', 'Window Server', 'GIT', 'Swift']
        teacher = []

        for _ in range(100):
            teacher.append(
                Teacher(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(25, 45),
                    course=random.choice(course),
                )
            )

        Teacher.objects.bulk_create(teacher)

        # for _ in range(100):
        #     Teacher.objects.create(
        #         first_name=fake.first_name(),
        #         last_name=fake.last_name(),
        #         age=random.randint(20, 40),
        #         course=random.choice(course),
        #     )
