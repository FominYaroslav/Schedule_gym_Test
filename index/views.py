from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from trainings.models import Training


class Search(ListView):
    model = Training
    template_name = "schedule.html"
    paginate_by = 12

    def get_queryset(self):

        name_get = self.request.GET.get("name")

        return Training.objects.filter(Q(name=name_get))


# Create your views here.
