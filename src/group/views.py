from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from group.forms import GroupCreateForm
from group.models import Group


def groups_all(request):
    # parse parameters
    param = [
        'course',
        'number_students_in_group',
        'start_group',
        'id',
    ]

    group_queryset = Group.objects.all()

    for param in param:
        value = request.GET.get(param)
        if value:
            group_queryset = group_queryset.filter(**{param: value})

    response = f'group: {group_queryset.count()}<br/>'

    for group in group_queryset:
        response += group.full_status() + '<br/>'

    return HttpResponse(response)


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {'create_form': form}

    return render(request, 'group_create.html', context=context)
