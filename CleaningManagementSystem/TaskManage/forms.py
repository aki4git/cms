from django.forms import ModelForm
from TaskManage.models import Place, Task

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ('name',)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name','user')