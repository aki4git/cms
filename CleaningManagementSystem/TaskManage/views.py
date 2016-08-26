from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from TaskManage.models import Place


# Create your views here.
def place_list(request):
    places = Place.objects.all().order_by('id')
    return render(request,
                  'TaskManage/place_list.html',
                  {'places':places})


class place_detail(ListView):
    context_object_name = 'tasks'
    template_name = 'TaskManage/place_detail.html'
    paginate_by = 10
    
    def get(self, request, *args, **kwargs):
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        users = place.users.all()
        tasks = place.tasks.all().order_by('id')
        self.object_list = tasks
        
        context = self.get_context_data(object_list=self.object_list, place=place, users=users)
        return self.render_to_response(context)
