from django.http import HttpResponse
from django.shortcuts import render  # noqa

from group.models import Group


def groups_all(request):
    request = Group.objects.count()
    group_queryset = Group.objects.full_status()

    response = f'group: {group_queryset} {request}<br/>'

    return HttpResponse(response)
