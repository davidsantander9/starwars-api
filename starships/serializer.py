from dataclasses import field
from urllib import response
from rest_framework import serializers
from starships.models import Starship

class StarshipSerializer(serializers.ModelSerializer):
  class Meta:
    model = Starship
    fields = '__all__'
    depth = 1