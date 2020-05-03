from django.db import models


# Create your models here.


class Group(models.Model):
    theme = models.CharField(max_length=32)
    created_group = models.DateTimeField(auto_now_add=True)

    @property
    def full_status(self) -> str:
        return f'{self.theme} {self.created_group}'
