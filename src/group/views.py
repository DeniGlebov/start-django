from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group


def groups_all(request):
    count = Group.objects.count()
    group_queryset = Group.objects.full_status()

    response = f'group: {group_queryset}<br/>'

    return HttpResponse(response)
