from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from teachers.forms import Teacher


@receiver(pre_save, sender=Teacher)
def teacher_pre_save(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(post_save, sender=Teacher)
def teacher_post_save(sender, instance, **kwargs):
    pass
