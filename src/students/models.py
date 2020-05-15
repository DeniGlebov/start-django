from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()  # models.IntegerField
    password = models.CharField(max_length=128, default='')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

    def inc_age(self) -> None:
        self.age += 1
        self.save()

    def __str__(self):
        return self.info()
