from django.shortcuts import render
from django.views.generic import ListView
from .models import Training

class Schedule(ListView):
    model =  Training
    template_name = 'schedule.html'