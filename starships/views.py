from starships.models import Starship
from starships.serializer import StarshipSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class StarshipViewSet(viewsets.ModelViewSet):
  queryset = Starship.objects.all()
  serializer_class = StarshipSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields ={'id_api': ['exact']}