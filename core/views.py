from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StateSerializer, GovernorSerializer

from .models import State, Governor

class StateList(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class GovernorList(ListAPIView):
    queryset =  Governor.objects.all()
    serializer_class = GovernorSerializer