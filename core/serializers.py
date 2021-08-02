from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from .models import State, Governor

class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ['state_name', 'capital']

class GovernorSerializer(ModelSerializer):
    class Meta:
        model = Governor
        fields = [('state'), 'name']