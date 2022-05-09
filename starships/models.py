from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Starship(models.Model):
  id_api = models.IntegerField(unique=True, blank=False)
  name = models.CharField(max_length=120, default='')
  model = models.CharField(max_length=120, default='')
  manufacturer = models.CharField(max_length=120, default='')
  cost_in_credits = models.CharField(max_length=120, default='')
  length = models.CharField(max_length=120, default='')
  max_atmosphering_speed = models.CharField(max_length=120, default='')
  crew = models.CharField(max_length=120, default='')
  passengers = models.CharField(max_length=120, default='')
  cargo_capacity = models.CharField(max_length=120, default='')
  hyperdrive_rating = models.CharField(max_length=120, default='')
  MGLT = models.CharField(max_length=120, default='')
  starship_class = models.CharField(max_length=120, default='')
  created = models.CharField(max_length=120, default='')
  edited = models.CharField(max_length=120, default='')
  url = models.CharField(max_length=120, default='')

