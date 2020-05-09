from django.db import models


# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=32, default='')

    @property
    def info_teacher(self) -> str:
        return f'{self.first_name} {self.last_name} {self.age}'

    def full_info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.course}'
