from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from students.forms import Student


@receiver(pre_save, sender=Student)
def student_pre_save(sender, instance, **kwargs):
    instance.phone = ''.join(i for i in instance.phone if i.isdigit())
    # instance.save()  # NEVER!


@receiver(post_save, sender=Student)
def student_post_save(sender, instance, **kwargs):
    print('post_save\n')
    # instance.profile.save()
