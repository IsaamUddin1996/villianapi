from django.shortcuts import render

from rest_framework import viewsets

from .serializers import VillianSerializer
from .models import Villian


class VillianViewSet(viewsets.ModelViewSet):
    queryset = Villian.objects.all().order_by('DOB')
    serializer_class = VillianSerializer
