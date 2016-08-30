from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from TaskManage.models import Place, Task
from TaskManage.forms import PlaceForm, TaskForm

# Create your views here.
@login_required
def place_list(request):
    places = Place.objects.all().order_by('id')
    return render(request,
                  'TaskManage/place_list.html',
                  {'places':places})


@login_required
def place_edit(request, place_id=None):
    if place_id:
        place = get_object_or_404(Place, pk=place_id)
    else:
        place = Place()
    
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('taskmanage:place_list')
    else:
        form = PlaceForm(instance=place)
    
    return render(request, 'taskmanage/place_edit.html', dict(form=form, place_id=place_id))


@login_required
def place_del(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.delete()
    return redirect('taskmanage:place_list')


class place_detail(ListView):
    context_object_name = 'tasks'
    template_name = 'TaskManage/place_detail.html'
    paginate_by = 10
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        users = place.users.all()
        tasks = place.tasks.all().order_by('id')
        self.object_list = tasks
        
        context = self.get_context_data(object_list=self.object_list, place=place, users=users)
        return self.render_to_response(context)


def task_edit(request, place_id, task_id=None):
    place = get_object_or_404(Place, pk=place_id)
    if task_id:
        task = get_object_or_404(Task, pk=task_id)
    else:
        task = Task()
    
    if request.method == 'POST':
        
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.place = place
            task.save()
            return redirect('taskmanage:place_detail', place_id=place_id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'taskmanage/task_edit.html', dict(form=form, place_id=place_id, task_id=task_id))


def task_del(request, place_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('taskmanage:place_detail', place_id=place_id)
