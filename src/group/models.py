import datetime

from django.db import models

from students.models import Student

from teachers.models import Teacher


class Group(models.Model):
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

    course = models.CharField("Course name", max_length=32, choices=course_list, default='Introduction')
    number_students_in_group = models.CharField("Person in group", max_length=2, default=14)
    start_group = models.DateField("Start date, example: 2020-12-24", default=datetime.date.today)
    # head = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    head = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='groups_head')
    curator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='groups_curator')

    def full_status(self) -> str:
        return f'{self.course} {self.number_students_in_group} {self.start_group} {self.head} {self.curator}'
