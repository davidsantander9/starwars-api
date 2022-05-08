from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Starship(models.Model):
  name = models.CharField(max_length=120, default='')
  model = models.CharField(max_length=120, default='')
  manufacturer = models.CharField(max_length=120, default='')
  cost_in_credits = models.IntegerField(default=0.0, validators=[MinValueValidator(0)])
  length = models.IntegerField(default=0.0, validators=[MinValueValidator(0)])
  max_atmosphering_speed = models.IntegerField(default=0.0, validators=[MinValueValidator(0)])
  crew = models.CharField(max_length=120, default='')
  passengers = models.IntegerField(default=0.0, validators=[MinValueValidator(0)])
  cargo_capacity = models.IntegerField(default=0.0, validators=[MinValueValidator(0)])
  hyperdrive_rating = models.CharField(max_length=120, default='')
  MGLT = models.CharField(max_length=120, default='')
  starship_class = models.CharField(max_length=120, default='')
  created = models.CharField(max_length=200, default='')
  edited = models.CharField(max_length=200, default='')
  url = models.CharField(max_length=200, default='')

