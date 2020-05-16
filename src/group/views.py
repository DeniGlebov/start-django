from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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

    return render(request, 'group-list.html', context={'group': group_queryset})


def index(request):
    return render(request, 'index.html')


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {'create_form': form}

    return render(request, 'group-create.html', context=context)


def edit_group(request, pk):
    try:
        group = get_object_or_404(Group, id=pk)
    except OverflowError:  # http://127.0.0.1:8000/students/edit/9999999999999999999
        raise Http404

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))
    elif request.method == 'GET':
        form = GroupCreateForm(instance=group)

    context = {'form': form, 'instance': group}

    return render(request, 'group-edit.html', context=context)


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return HttpResponseRedirect(reverse('group:list'))
