from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from trainings.models import Training

from .serializers import TrainingSerializer


class TrainingViewSet(viewsets.ModelViewSet):

    serializer_class = TrainingSerializer
    queryset = Training.objects.all().order_by("time")
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
