from django.db import models


class Teacher(models.Model):
    PHP = 'PHP'
    Java = 'Java'
    Python = 'Python'
    Ruby = 'Ruby'
    Rust = 'Rust'
    Swift = 'Swift'
    Linux = 'Linux'
    Introduction = 'Introduction'

    course_list = (
        [PHP, 'PHP'],
        [Java, 'Java'],
        [Python, 'Python'],
        [Ruby, 'Ruby'],
        [Rust, 'Rust'],
        [Swift, 'Swift'],
        [Linux, 'Linux'],
        [Introduction, 'Introduction'],
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=32, choices=course_list, default='Introduction')

    @property
    def info_teacher(self) -> str:
        return f'{self.first_name} {self.last_name} {self.age}'

    def full_info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.course}'
