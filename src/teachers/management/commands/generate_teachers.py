import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random teacher'  # noqa

    def handle(self, *args, **options):
        fake = Faker()

        course = ['PHP', 'Java', 'Python', 'Ruby', 'Rust', 'Swift', 'Linux', 'Introduction']
        teacher = []

        for _ in range(50):
            teacher.append(
                Teacher(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(25, 45),
                    course=random.choice(course),
                )
            )

        Teacher.objects.bulk_create(teacher)
