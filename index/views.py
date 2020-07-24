from django.shortcuts import render
from trainings.models import Training
from django.views.generic import ListView
from django.db.models import Q

def home(request):

    return render(request, 'index.html', context)

class Search(ListView):
    model = Training
    template_name ='schedule.html'
    paginate_by = 12

    def get_queryset(self):


        name_get = self.request.GET.get('name')

        return Training.objects.filter(
            Q(name = name_get)
        )
# Create your views here.
