from django.shortcuts import render
from .serializers import TrainingSerializer
from rest_framework import viewsets
from trainings.models import Training
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# Create your views here.
class TrainingViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all().order_by("time")
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
